from src.models import PokeDB

def save_pokemon(db, data):
    pokemon = PokeDB(
        id=data["id"],
        name=data["name"],
        height=data["height"],
        weight=data["weight"],
        types=[item["type"]["name"] for item in data["types"]],
        sprites={
            "front_default": data["sprites"]["front_default"]
        }
    )

    db.add(pokemon)
    db.commit()