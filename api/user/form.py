from app.database import db
from mongoengine import *
from app.error import *
from utils.formatter import Formatter

class address(EmbeddedDocument):
    city = db.StringField(required=True)
    state = db.StringField(required=True)
    zip = db.StringField()

class user(db.Document):
    name = db.StringField(required=True)
    address = db.EmbeddedDocumentField(address, required=True)

def get_user(data):
    schema = {
        "name": "name",
        "city": "address.city"
    }
    return Formatter(data, schema).format()

class user_format(Formatter):
    def __init__(self, data):
        schema = {
            "name": "name",
            "city": "address.city"
        }
        super().__init__(data, schema)