from fastapi import FastAPI, Response
import plotly.express as px
from collections import Counter
import pandas as pd
import country_converter as coco


app = FastAPI()


@app.get("/test")
async def test():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    fig_bytes = fig.to_image(format="png")
    return Response(content=fig_bytes, media_type="image/png")


@app.get("/plot")
async def plot():
    creatures = pd.read_csv("./creature.psv", sep="|")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counts = Counter(creature[0] for creature in creatures["name"])
    y = {letter: counts.get(letter, 0) for letter in letters}
    fig = px.histogram(
        x=list(letters),
        y=y,
        title="Creature Names",
        labels={"x": "Initial", "y": "Initial"},
    )
    fig_bytes = fig.to_image(format="png")
    return Response(content=fig_bytes, media_type="image/png")


@app.get("/map")
def map():
    creatures = pd.read_csv("./creature.psv", sep="|")
    iso2_codes = set(country for country in creatures["country"])
    iso3_codes = coco.convert(names=iso2_codes, to="ISO3")
    fig = px.choropleth(locationmode="ISO-3", locations=iso3_codes)
    fig_bytes = fig.to_image(format="png")
    return Response(content=fig_bytes, media_type="image/png")
