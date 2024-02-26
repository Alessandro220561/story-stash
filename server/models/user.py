from config import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String)
    readings = db.relationship('ReadingLog', backref='user')
    user_log = db.relationship('UserLog', backref='user')

    def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.email}>'