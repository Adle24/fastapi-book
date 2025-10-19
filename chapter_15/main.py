from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from typing import Generator
from fastapi.staticfiles import StaticFiles
from pathlib import Path


top = Path(__file__).resolve().parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=f"{top}/static"), name="static")


def gen_file(path: str) -> Generator:
    with open(path, "rb") as f:
        yield f.read()


@app.post("/small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)} bytes"


@app.post("/big")
async def upload_big_file(big_file: UploadFile) -> str:
    return f"file size: {big_file.size}, file name: {big_file.filename}"


@app.get("/small/{name}")
async def download_small_file(name: str):
    return FileResponse(name)


@app.get("/big/{name}")
async def download_big_file(name: str):
    gen_expr = gen_file(name)
    response = StreamingResponse(gen_expr, status_code=200)
    return response
