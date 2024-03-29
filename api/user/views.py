from app import app
from .form import user, user_format
from flask import request
from app.error import *

@app.route("/user/create", methods=['POST'])
def create_user():
    data = request.get_json()
    create = user(**data).save()
    return create.to_json()

@app.route("/user/get")
def get_user_data():
    id = request.args['id']
    result = user_format().format(user.objects(), many=True)
    return result