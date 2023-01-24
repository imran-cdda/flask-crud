from app import app
from flask import request
from app.database import db
from mongoengine import *
from app.error import *

class property(db.Document):
    name = db.StringField(unique=True, required=True)
    address = db.StringField()

@app.route('/insert', methods=['POST'])
def create_property():
    data = request.get_json()
    create_prop = property(**data).save()
    return create_prop.to_json()

@app.route('/get')
def get_property():
    get_property = property.objects()
    return get_property.to_json()

if __name__ == '__main__':
    app.run(debug=True)