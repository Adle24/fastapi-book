from fastapi import FastAPI
from cryptids.src.web import explorer, creature, user
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)


@app.get("/")
def top():
    return {"message": "top here"}


@app.get("/echo/{thing}")
def echo(thing):
    return {"thing": thing}
