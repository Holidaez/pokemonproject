from .models import Pokemon, Item
from alembic import op

op.bulk_insert(Pokemon, [
      {
        number: 1,
        image_url: '/images/pokemon_snaps/1.svg',
        name: 'Bulbasaur',
        attack: 49,
        defense: 49,
        type: 'grass',
        moves:'tackle,vine whip'
        captured: true
      },
      {
        number: 2,
        imageUrl: '/images/pokemon_snaps/2.svg',
        name: 'Ivysaur',
        attack: 62,
        defense: 63,
        type: 'grass',
        moves: "tackle,vine whip,razor leaf"
        captured: true
      },
      {
        number: 3,
        imageUrl: '/images/pokemon_snaps/3.svg',
        name: 'Venusaur',
        attack: 82,
        defense: 83,
        type: 'grass',
        moves: "tackle,vine whip, razor leaf"
        captured: true
      },
      {
        number: 4,
        imageUrl: '/images/pokemon_snaps/4.svg',
        name: 'Charmander',
        attack: 52,
        defense: 43,
        type: 'fire',
        moves: "scratch,ember,metal claw"
        captured: true
      },
      {
        number: 5,
        imageUrl: '/images/pokemon_snaps/5.svg',
        name: 'Charmeleon',
        attack: 64,
        defense: 58,
        type: 'fire',
        moves:"scratch,ember,metal claw,flamethrower"
        captured: true
      },
      {
        number: 6,
        imageUrl: '/images/pokemon_snaps/6.svg',
        name: 'Charizard',
        attack: 84,
        defense: 78,
        type: 'fire',
        moves:"flamethrower,wing attack,slash,metal claw"
        captured: true
      },
      {
        number: 7,
        imageUrl: '/images/pokemon_snaps/7.svg',
        name: 'Squirtle',
        attack: 48,
        defense: 65,
        type: 'water',
        moves:"tackle,bubble,water gun",
        captured: true
      },
    ])
