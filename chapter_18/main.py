from pathlib import Path
from fastapi import FastAPI, Body, Request
from fastapi.templating import Jinja2Templates
from random import choice
import pandas as pd
from collections import Counter, defaultdict
from fastapi.middleware.cors import CORSMiddleware


HIT = "H"
MISS = "M"
CLOSE = "C"

def get_score(actual: str, guess: str) -> str:
    length: int = len(actual)

    if len(guess) != length:
        return "ERROR"

    actual_counter = Counter(actual)
    guess_counter = defaultdict(int)
    result = [MISS] * length

    for pos, letter in enumerate(guess):
        if letter == actual[pos]:
            result[pos] = HIT
            guess_counter[letter] += 1

    for pos, letter in enumerate(guess):
        if result[pos] == HIT:
            continue
        guess_counter[letter] += 1

        if (letter in actual and guess_counter[letter] <= actual_counter[letter]):
            result[pos] = CLOSE

    result = "".join(result)
    return result


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/game")
async def game_start(request: Request):
    creatures = pd.read_csv("./creature.psv", sep="|")
    creature_name = choice(creatures["name"])
    top = Path(__file__).resolve().parent
    templates = Jinja2Templates(directory=f"{top}/template")
    return templates.TemplateResponse("game.html", {
        "request": request,
        "word": creature_name,
    })

@app.post("/game")
async def game_step(word: str = Body(), guess: str = Body()):
    score = get_score(word, guess)
    return score

