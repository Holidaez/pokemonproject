from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .item import Item
from .pokemon import Pokemon
from .pokemon_type import types
