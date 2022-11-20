import json
import random 
import sys
import requests
from bs4 import BeautifulSoup
from collections import defaultdict, Counter

# FIXME This is not working yet, websites actually detect i'm a robot 🤖
# Take an url in parameter and return the lyrics of the artist
def scrape_text(domain = 'https://www.azlyrics.com', artist = 'damso'): 
    artist_url = '/' + artist[0] + '/' + artist + '.html' # if artist is damso, the url will be /d/damso.html
    url = 'https://paroles2chansons.lemonde.fr/paroles-damso'
    response = requests.get(url)
    text = []
    if response.ok: 
        soup = BeautifulSoup(response.text, 'html.parser')
        listalbum_items = soup.find_all('div', class_='info-item') 
        links = [domain+item.find('a')['href'] for item in listalbum_items]
        nb_links = len(links) if len(links) < 30 else 30
        cnt = 0
        for link in links:
            if cnt < 30: 
                cnt += 1
                print('scraping link {}/{}'.format(cnt, nb_links))
                response = requests.get(link)
                print(link)
                print(response)
                if response.ok:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    lyrics = soup.find_all('div', class_='block-spacing-medium')
                    print(lyrics)
                    text.append(lyrics)
        return text

# result = scrape_text()
# print(result)

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
def generate_text(markov_model, speech_size=300):
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



# damso_text = open('texts/damso.txt', 'r').read()
# model = build_markov_model(damso_text, state_size=5)

# json.dump(model, open("./jsons/model.json", "w"))

# generate_text(model)