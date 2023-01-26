from app.database import db
from mongoengine import *
from app.error import *
from utils.formatter import DataFormatter
from api.user.form import user

class corod(EmbeddedDocument):
    lat = db.StringField(required=True)
    lng = db.StringField(required=True)

class address(EmbeddedDocument):
    city = db.StringField(required=True)
    state = db.StringField(required=True)
    coordinate = db.EmbeddedDocumentField(corod, required=True)

class property(db.Document):
    title = db.StringField(required=True)
    # address = db.EmbeddedDocumentField(address, required=True)
    address = db.StringField(required=True)
    user = db.ReferenceField(user, required=True)

class pro_format(DataFormatter):
    id = "_id"
    name = "title"
    user = {
        "name": "user.name",
        "city": "user.address.city"
    }