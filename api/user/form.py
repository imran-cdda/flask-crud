from app.database import db
from mongoengine import *
from app.error import *
from utils.formatter import DataFormatter

class corod(EmbeddedDocument):
    lat = db.StringField(required=True)
    lng = db.StringField(required=True)

class address(EmbeddedDocument):
    city = db.StringField(required=True)
    state = db.StringField(required=True)
    coordinate = db.EmbeddedDocumentField(corod, required=True)

class user(db.Document):
    name = db.StringField(required=True)
    address = db.EmbeddedDocumentField(address, required=True)

class user_format(DataFormatter):
    name = "name"
    lat = "address.coordinate.lat"