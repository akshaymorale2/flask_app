from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
