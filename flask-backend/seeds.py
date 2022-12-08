from app.models import Pokemon, Item,db
from app import app
import random, math
with app.app_context():
  db.drop_all()
  db.create_all()
  pokemon1 = Pokemon(
    number= 1,
    attack= 49,
    defense= 49,
    image_url= '/images/pokemon_snaps/1.svg',
    name= 'Bulbasaur',
    type= 'grass',
    moves='tackle,vine whip',
    catch_rate=0.31,
    encounter_rate=0.33,
    captured= True
  )
  pokemon2 = Pokemon(
    number= 2,
    attack= 49,
    defense= 49,
    image_url= '/images/pokemon_snaps/1.svg',
    name= 'vileploom',
    type= 'grass',
    moves='tackle,vine whip',
    catch_rate=0.31,
    encounter_rate=0.33,
    captured= True
  )
  pokemon3 = Pokemon(
    number= 3,
    attack= 49,
    defense= 49,
    image_url= '/images/pokemon_snaps/1.svg',
    name= 'Charizard',
    type= 'fire',
    moves='tackle,fire',
    catch_rate=0.31,
    encounter_rate=0.33,
    captured= True
  )
  pokemon4 = Pokemon(
    number= 4,
    attack= 49,
    defense= 49,
    image_url= '/images/pokemon_snaps/1.svg',
    name= 'Gloom',
    type= 'grass',
    moves='tackle,vine whip',
    catch_rate=0.31,
    encounter_rate=0.33,
    captured= True
  )
  pokemon5= Pokemon(
    number= 5,
    attack= 49,
    defense= 49,
    image_url= '/images/pokemon_snaps/1.svg',
    name= 'Squirtle',
    type= 'water',
    moves='tackle,vine whip',
    catch_rate=0.31,
    encounter_rate=0.33,
    captured= True
  )
  pokemon6 = Pokemon(
    number= 6,
    attack= 49,
    defense= 49,
    image_url= '/images/pokemon_snaps/1.svg',
    name= 'Ditto',
    type= 'grass',
    moves='tackle,vine whip',
    catch_rate=0.31,
    encounter_rate=0.33,
    captured= True
  )
  pokemon7 = Pokemon(
    number= 7,
    attack= 49,
    defense= 49,
    image_url= '/images/pokemon_snaps/1.svg',
    name= 'charmander',
    type= 'fire',
    moves='tackle,vine whip',
    catch_rate=0.31,
    encounter_rate=0.33,
    captured= True
  )
  all_pokemon=[pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,pokemon7]
  add_pokemon= [db.session.add(pokemon) for pokemon in all_pokemon]
  db.session.commit()
  print("Pokemon seeded")

# def random100():
#   return math.floor(random.randint(0,100)) + 1
# def randomImage():
#   images = [
#     "/images/pokemon_berry.svg",
#     "/images/pokemon_egg.svg",
#     "/images/pokemon_potion.svg",
#     "/images/pokemon_super_potion.svg",
#   ]
#   index = math.floor(random.randit()* len(images))
#   return images[index]
# def mygenerator():
#   item, items = 0,[]
#   while item < n:
#     items.append(item)
#     item += 1
#     return items
  item1 = Item(
    happiness=100,
    image_url="/images/pokemon_berry.svg",
    name="Occa Berry",
    price=75,
    pokemon_id=1
  )
  item2 = Item(
    happiness=100,
    image_url="/images/pokemon_potion.svg",
    name="Potion",
    price=75,
    pokemon_id=2
  )
  item3 = Item(
    happiness=100,
    image_url= "/images/pokemon_potion.svg",
    name="Fancy Purse",
    price=75,
    pokemon_id=3
  )
  item4 = Item(
    happiness=100,
    image_url="/images/pokemon_potion.svg",
    name="Mini Bulbasaur toy",
    price=75,
    pokemon_id=4
  )
  item5 = Item(
    happiness=100,
    image_url="/images/pokemon_potion.svg",
    name="another one",
    price=75,
    pokemon_id=5
  )
  item6 = Item(
    happiness=100,
    image_url="/images/pokemon_super_potion.svg",
    name="Captain crunch cereal",
    price=75,
    pokemon_id=6
  )
  item7 = Item(
    happiness=100,
    image_url="/images/pokemon_super_potion.svg",
    name="A delicious sandwich",
    price=75,
    pokemon_id=7
  )
  all_item=[item1,item2,item3,item4,item5,item6,item7]
  add_item= [db.session.add(item) for item in all_item]
  db.session.commit()
  print("Items seeded")
