from fastapi import FastAPI, Depends


def user_dep(name: str, password: str):
    return {"name": name, "valid": True}


def check_dep(name: str, password: str):
    if not name:
        print("there is no name")


def gloabal_dep():
    pass


app = FastAPI(dependencies=[Depends(gloabal_dep)])


@app.get("/user")
async def get_user(user: dict = Depends(user_dep)) -> dict:
    return user


@app.get("/check_user", dependencies=[Depends(user_dep)])
async def check_user() -> bool:
    return True
