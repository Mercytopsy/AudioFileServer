from flask_mongoengine import MongoEngine
from settings import DB, DATABASE_USERNAME, DATABASE_PASSWORD
import os

db = MongoEngine()

def initialize_db(app):
    app.config['MONGODB_SETTINGS'] = {
    'db': os.getenv(DB),
    'username':os.getenv(DATABASE_USERNAME),
    'password':os.getenv(DATABASE_PASSWORD)
}
    db.init_app(app)


