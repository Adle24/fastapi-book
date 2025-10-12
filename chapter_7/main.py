from fastapi import FastAPI, Header


app = FastAPI()


@app.get("/greet/{name}")
async def greet(name: str, age: int, header: str = Header()):
    return {"message": f"Hello, {name}! You are {age} years old.", "header": header}
