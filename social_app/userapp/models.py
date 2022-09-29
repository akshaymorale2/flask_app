from datetime import datetime
from .. import db


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(100))
    profilePhoto = db.Column(db.String(100), default='default_profile_picture.png')
    dateOfBirth = db.Column(db.String(255))
    contactNumber = db.Column(db.String(12))
    gender = db.Column(db.String(10))
    is_verified = db.Column(db.Boolean(), default=True)
    shouts_user = db.relationship('Shouts')

    def __repr__(self):
        return f"<Users {self.username}>"

    def to_json(self):
        return {"username": self.username,
                "id": self.id,
                "is_verified": self.is_verified}


class Shouts(db.Model):
    __tablename__ = 'shout'
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime(), default=datetime.utcnow)
    textdata = db.Column(db.String(255), nullable=True)
    type = db.Column(db.String(100))
    filename = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"<Shouts {self.id}>"
