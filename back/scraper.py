# --------------------------------------------------------------------
# /!\ Make sure to be in back folder to execute this python script /!\ 
# --------------------------------------------------------------------

import requests
import random
import yaml
import pandas as pd
from bs4 import BeautifulSoup

# Constants
NB_PROXIES = 10
IP_CHECK_URL = "https://httpbin.org/ip" # Url to check if the proxy is working
FREE_PROXIES_URL = "https://free-proxy-list.net/"


with open('./src/headers.yml') as f_headers:
    browser_headers = yaml.safe_load(f_headers)

with open('./src/user_agents.yml') as f_user_agents:
    user_agents = yaml.safe_load(f_user_agents)

# Scrape a list of proxies from https://free-proxy-list.net/
def scrape_proxies(): 
    response = requests.get(FREE_PROXIES_URL)
    proxy_list = pd.read_html(response.text)[0]
    proxy_list['url'] = 'http://' + proxy_list['IP Address'] + ':' + proxy_list['Port'].astype(str)
    proxy_list.head()
    https_proxies = proxy_list[proxy_list['Https'] == "yes"] # Select only https proxies
    return select_good_proxies(https_proxies)

# Get a list of proxies in params and return a good proxies array, checked by httpbin.org/ip
def select_good_proxies(proxies):
    good_proxies = []
    headers = browser_headers["Chrome"] # Using Chrome headers, no reason to use another one
    print("Searching for {} proxies...".format(NB_PROXIES))
    for proxy_url in proxies["url"]: # For each proxy in the list
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }

        try: # We make a request to httpbin.org/ip and see the response
            response = requests.get(IP_CHECK_URL, headers=headers, proxies=proxies, timeout=2)
            good_proxies.append(proxy_url)
            print("{}/{} - Good proxy: {}".format(len(good_proxies), NB_PROXIES, proxy_url))
        except Exception:
            pass
            
        if len(good_proxies) >= NB_PROXIES:
            break
    # print("Good proxies: {}\n".format(good_proxies))
    return good_proxies


# Scrape the artist page to get all the songs
# Then use our proxy/headers protection to scrappe all lyrics from the songs and save them in jsons/*artist_name*.json
def scrape_text(artist, domain = 'https://www.azlyrics.com'):
    good_proxies = scrape_proxies() 

    artist_url = '/' + artist[0] + '/' + artist + '.html' # if artist is damso, the url will be /d/damso.html
    url = domain + artist_url
    response = requests.get(url) # The first request to access the artist page is not under protection
    if response.ok: 
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='listalbum-item')
        links = [domain+item.find('a').get('href') for item in items] # Get all the links to the songs
        nb_links = len(links) if len(links) < 200 else 200 # We don't want to scrappe too much songs, so we limit 
        cnt = 1
        for link in links: # For each song
            if cnt <= nb_links: 
                while True: 
                    print('---------')
                    print('scraping link {}/{}'.format(cnt, nb_links))
                    print(link+'\n')
                    
                    try: 
                        proxy_url = random.choice(good_proxies) # Get a random proxy from the good proxies list
                        proxies = proxies = {
                            "http": proxy_url,
                            "https": proxy_url
                        }
                        browser, headers = random.choice(list(browser_headers.items())) # Get a random header from headers.yml
                        # print(f"\n Using {browser} headers \n")
                        
                        response = requests.get(link, headers=headers, proxies=proxies, timeout=2)
                        print(response.text)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        lyrics_node = soup.find('div', class_='ringtone').find_next_sibling('div') # Target the div with the lyrics
                        lyrics = lyrics_node.text
                        print(lyrics)
                        with open(f'./texts/{artist}.txt', 'a+') as txt_file: # Save the lyrics in jsons/*artist_name*.json
                            txt_file.write(lyrics)
                        print(e)
                        cnt += 1 # Increment the counter if all went well
                    
                    except Exception as e:
                        print(f"Proxy {proxy_url} failed", e)
                        if len(good_proxies) > 1:
                            good_proxies.remove(proxy_url) # Remove the proxy from the good proxies list if it failed
                            print(f"Good proxies left : {good_proxies}")
                        else: 
                            print("No more proxies left, exiting")
                            exit()
             
scrape_text('angle');