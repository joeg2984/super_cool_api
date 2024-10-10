from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from sqlmodel import Session, select
from models import retrovideogame
from database import create_db_and_tables, engine

@asynccontextmanager
async def lifespan(_app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/games/", response_model=list[retrovideogame])
def get_games():
    with Session(engine) as session:
        games = session.exec(select(retrovideogame)).all()
        return games

@app.post("/games/", response_model=retrovideogame)
def add_game(game: retrovideogame):
    with Session(engine) as session:
        session.add(game)
        session.commit()
        session.refresh(game)
        return game

@app.get("/games/{game_id}", response_model=retrovideogame)
def get_game(game_id: int):
    with Session(engine) as session:
        game = session.get(retrovideogame, game_id)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")
        return game

@app.delete("/games/{game_id}", response_model=dict)
def delete_game(game_id: int):
    with Session(engine) as session:
        game = session.get(retrovideogame, game_id)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")
        session.delete(game)
        session.commit()
        return {"detail": "Game deleted successfully"}
