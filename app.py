from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.data import SessionLocal
from src.models import PokeDB
from src.seed import set_database
from celery_app import celery_app
from celery.result import AsyncResult

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def setData():

    task = set_database.delay()

    return {"task_id": task.id, "message": "Setting DB."}

@app.get("/status/{task_id}")
def task_status(task_id: str):

    task = AsyncResult(task_id, app=celery_app)

    return {"status": task.status}

@app.get("/pokemon")
async def get_pokemon(page: int = 1, limit: int = 10, db:Session = Depends(get_db)):
    if page <1 or limit <1:
        raise HTTPException(status_code=400, detail="Page or limit with invalid values.")

    pokemonList = db.query(PokeDB).offset((page - 1)*limit).limit(limit).all()

    if not pokemonList:
        raise HTTPException(status_code=404, detail="Pokemon not found!")
    else:
        response = ["Pokemon: "]
        for item in pokemonList:
            response.append({
                "id": item.id, 
                "name": item.name, 
                "height": item.height, 
                "weight": item.weight, 
                "types": item.types,
                "sprites": item.sprites})
        return {"pokemonList": response}

@app.get("/pokemon/{id}")
async def get_pokemon_per_id(id: int, db: Session = Depends(get_db)):

    pokemon = db.query(PokeDB).filter(PokeDB.id == id).first()

    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found!")
    else:
        return {
            "id": pokemon.id, 
            "name": pokemon.name, 
            "height": pokemon.height, 
            "weight": pokemon.weight, 
            "types": pokemon.types,
            "sprites": pokemon.sprites
        }