from app import app
from .form import property, pro_format
from flask import request
from app.error import *
import json

@app.route("/property/create", methods=['POST'])
def create_property():
    data = request.get_json()
    create = property(**data).save()
    return create.to_json()

@app.route("/property")
def get_property():
    if "id" in request.args:
        id = request.args['id']
        get_property = property.objects.get(id = id)
        rs = pro_format().format(get_property, ref=["user"])
        return rs
    get_property = property.objects()
    rs = pro_format().format(get_property, many=True, ref=["user"])
    return rs