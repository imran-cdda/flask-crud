from flask_mongoengine import MongoEngine
from app import app

app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'localhost',
    'port': 27017,
    'connect': False
}

db = MongoEngine(app)