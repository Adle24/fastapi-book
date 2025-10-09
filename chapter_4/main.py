from fastapi import FastAPI
import asyncio


app = FastAPI()


@app.get("/hi")
async def greet():
    await asyncio.sleep(5)
    return {"hello": "world"}
