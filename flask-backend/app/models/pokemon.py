from .models import db
class Pokemon(db.Model):
    number=db.Column(db.Integer, nullable=False, unique:True, NumberRange(min=1,max=None))
    attack=db.Column(db.Integer,nullable=False)
    defense=db.Column(db.Integer, nullable=False)
    image_url=db.Column(db.String(255), nullable=False)
    name=db.Column(db.String(255),nullable=False)
    type=db.Column(db.String(255),nullable=False)
    moves=db.Column(db.String(255),nullable=True) #Needs updating
    encounter_rate=db.Column(db.Float, nullable=False)
    catch_rate=db.Column(db.Float(precision=2,asdecimal=True), nullable=False)
    captured=db.Column(db.Boolean, nullable=False)
