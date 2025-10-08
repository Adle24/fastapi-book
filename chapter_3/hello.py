from fastapi import FastAPI, Body, Header, Response

app = FastAPI()


@app.get("/hi")
async def greet(who: str):
    return f"Hello, {who}!"


@app.post("/hi")
async def post_greet(who: str = Body(embed=True)):
    return f"Hello, {who}!"


@app.post("/hi-header")
async def post_greet_header(who: str = Header()):
    return f"Hello, {who}!"


@app.post("/agent")
async def get_agent(user_agent: str = Header()):
    return user_agent


@app.get("/happy")
async def happy(status_code=200):
    return ":)"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"
