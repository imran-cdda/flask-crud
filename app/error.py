from app import app
from mongoengine.errors import ValidationError, NotUniqueError

@app.errorhandler(Exception)
def handle_error(error):
    response = {"error":str(error)}
    return response, 500

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = {"error":error.to_dict()}
    return response, 422

@app.errorhandler(NotUniqueError)
def handle_not_unique_error(error):
    response = {"error":str(error)}
    return response, 422