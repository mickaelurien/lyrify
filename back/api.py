from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import markov

app = FastAPI()

origins = ['http://127.0.0.1:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/{artist}")
def get_lyrics_by_artist(artist: str):
    return markov.generate_lyrics(artist)