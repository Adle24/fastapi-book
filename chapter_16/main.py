from fastapi import FastAPI, Form, Request
from pathlib import Path
from fastapi.templating import Jinja2Templates


app = FastAPI()

top = Path(__file__).resolve().parent
template_obj = Jinja2Templates(directory=f"{top}/template")

exploeres = [
    {
        "name": "Askar Adilet",
        "country": "Kazakhstan",
        "description": "Kazakh Explorer",
    }
]

creatures = [
    {
        "name": "Yeti",
        "country": "USA",
        "description": "bear like monster",
        "area": "Alaska",
        "aka": "Mock",
    }
]


@app.post("/greet")
def greet(name: str = Form()):
    return {"message": f"Hello, {name}!"}


@app.get("/list")
def explorer_list(request: Request):
    return template_obj.TemplateResponse(
        "list.html",
        {
            "request": request,
            "explorers": exploeres,
            "creatures": creatures,
        },
    )
