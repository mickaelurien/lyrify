import json
import random 
import re
import yaml
import sys
import requests
import markovify
import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict, Counter

with open('headers.yml') as f_headers:
    browser_headers = yaml.safe_load(f_headers)

with open('user_agents.yml') as f_user_agents:
    user_agents = yaml.safe_load(f_user_agents)

# Scrape a list of proxies from https://free-proxy-list.net/
def scrape_proxies(): 
    response = requests.get('https://free-proxy-list.net/')
    proxy_list = pd.read_html(response.text)[0]
    proxy_list['url'] = 'http://' + proxy_list['IP Address'] + ':' + proxy_list['Port'].astype(str)
    proxy_list.head()
    https_proxies = proxy_list[proxy_list['Https'] == "yes"] # Select only https proxies
    return select_good_proxies(https_proxies)

# Get a list of proxies in params and return a good proxies array, checked by httpbin.org/ip
def select_good_proxies(proxies, nb_needed=15):
    url = "https://httpbin.org/ip"
    good_proxies = []
    headers = browser_headers["Chrome"] # Using Chrome headers, no reason to use another one
    print("Searching for {} proxies...".format(nb_needed))
    for proxy_url in proxies["url"]: # For each proxy in the list
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }

        try: # We make a request to httpbin.org/ip and see the response
            response = requests.get(url, headers=headers, proxies=proxies, timeout=2)
            good_proxies.append(proxy_url)
            print("{}/{} - Good proxy: {}".format(len(good_proxies), nb_needed, proxy_url))
        except Exception:
            pass
            
        if len(good_proxies) >= nb_needed:
            break
    # print("Good proxies: {}\n".format(good_proxies))
    return good_proxies
    

# Scrape the artist page to get all the songs
# Then use our proxy/headers protection to scrappe all lyrics from the songs and save them in jsons/*artist_name*.json
def scrape_text(domain = 'https://www.azlyrics.com', artist = 'damso'):
    good_proxies = scrape_proxies() 
        
    artist_url = '/' + artist[0] + '/' + artist + '.html' # if artist is damso, the url will be /d/damso.html
    url = domain + artist_url
    response = requests.get(url) # The first request to access the artist page is not under protection
    if response.ok: 
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='listalbum-item')
        links = [domain+item.find('a').get('href') for item in items] # Get all the links to the songs
        # print(links)
        nb_links = len(links) if len(links) < 200 else 200 # We don't want to scrappe too much songs, so we limit 
        cnt = 1
        # lyrics = ''
        for link in links: # For each song
            if cnt <= nb_links: 
                print('scraping link {}/{}'.format(cnt, nb_links))
                browser, headers = random.choice(list(browser_headers.items())) # Get a random header from headers.yml
                print(f"\n Using {browser} headers \n")
                proxy_url = random.choice(good_proxies) # Get a random proxy from the good proxies list
                proxies = proxies = {
                    "http": proxy_url,
                    "https": proxy_url
                }
                try: 
                    response = requests.get(link, headers=headers, proxies=proxies, timeout=2)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    main_div = soup.find('div', class_='ringtone').find_next_sibling('div') # Target the div with the lyrics
                    lyrics = main_div.text
                    cnt += 1 # Increment the counter if all went well
                    print(lyrics)
                    with open(f'texts/{artist}.txt', 'a+', encoding="utf-8") as txt_file: # Save the lyrics in jsons/*artist_name*.json
                        # json.dump(lyrics, json_file)
                        txt_file.write(lyrics) 
                except Exception:
                    print(f"Proxy {proxy_url} failed")
        
                

# Build the markov model, return a dictionary with the state as key and the next state with the probability as value
# e.g : { "hello" : {"w" : 1} }
# that means the world "hello" is followed by "w" 1 time (maybe because the text was 'hello world')
def build_markov_model(train_text, state_size=1):
    markov_model = defaultdict(Counter)
    for i in range(len(train_text) - state_size):
        state = train_text[i:i + state_size]
        next_state = train_text[i + state_size]
        markov_model[state][next_state] += 1
    return markov_model

# Generate the word from the markov model
def generate_text(markov_model, speech_size=600):
    all_done = False
    speech = []

    while not all_done:
        this_state = random.choice(list(markov_model))
        speech += list(this_state)
        
        for i in range(speech_size):
            population = list(markov_model[this_state])
            weight = markov_model[this_state].values()
            if len(population) == 0:
                break

            next_state = random.choices(population, weight)[0]
            speech.extend(next_state)

            if (len(speech) >= speech_size):
                all_done = True
                break

            this_state = this_state[:1] + speech[-1]
    print(''.join(speech))


scrape_text()
# damso_text = json.load(open('jsons/damso.json', 'r'))
with open('./texts/damso.txt', 'r') as f:
    damso_text =  f.readlines()


# Use our markov model 
# model = build_markov_model(damso_text, state_size=8)
# print('-------------------------------------------------------')
# generate_text(model)

# Use the markovify library
damso_model = markovify.Text(damso_text, state_size=3)

# print('------------------------- FINAL -----------------------------\n')
# # print('Titre : ', damso_model.make_short_sentence(20) + ' - Damso')

# def generate_lyrics():
#     nb_couplet = 3
#     lyrics = ''
#     while nb_couplet > 0:
#         couplet = ''
#         nb_lines = 4
#         while nb_lines > 0:
#             line = damso_model.make_short_sentence(2000)
#             if (line):
#                 couplet += line + '\n'
#                 nb_lines -= 1
#         lyrics += '\n' + couplet + '\n'
#         nb_couplet -= 1
#     return lyrics

# print(generate_lyrics())