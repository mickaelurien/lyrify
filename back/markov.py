import json
import random
import markovify

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

# print(generate_lyrics('booba'))