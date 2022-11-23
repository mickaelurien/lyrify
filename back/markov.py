import json
import random
import re
import sys
import requests
import markovify

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

def generate_lyrics(artist):
    with open(f'./texts/{artist}.txt', 'r', encoding='utf-8') as f:
        data =  f.readlines()
    model = markovify.Text(data, state_size=3)
    nb_couplet = 3
    lyrics = ''
    while nb_couplet > 0:
        couplet = ''
        nb_lines = 4
        while nb_lines > 0:
            line = model.make_short_sentence(2000)
            if (line):
                couplet += line + '\n'
                nb_lines -= 1
        lyrics += '\n' + couplet + '\n'
        nb_couplet -= 1
    return lyrics

print(generate_lyrics('booba'))