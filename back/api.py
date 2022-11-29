import os
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import markov

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

origins = [os.environ.get('FRONT_URL')]

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