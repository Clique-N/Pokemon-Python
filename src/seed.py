from src.data import SessionLocal, Base, engine
from src.models import PokeDB
from src.pokeapi import get_pokemon
from src.repository import save_pokemon
from celery_app import celery_app

@celery_app.task
def set_database():

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        for pokemon_id in range(1, 152):
            print(f"Getting Pokemon {pokemon_id}...")

            pokemon = get_pokemon(pokemon_id)

            if pokemon:
                save_pokemon(db, pokemon)
    finally:
        db.close()

    return "DB sucefully populated."
