from fastapi import FastAPI
from .services import get_magnificent_7, get_team_magnificent_7

app = FastAPI()


@app.get("/magnificent-7")
def magnificent_7():
    return get_magnificent_7()


@app.get("/magnificent-7/team/{team_id}")
def team_magnificent_7(team_id: int):
    return get_team_magnificent_7(team_id)
