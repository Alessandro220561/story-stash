from config import db, bcrypt
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String)
    _password_hash = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))


    readings = db.relationship('ReadingLog', backref='user')
    user_log = db.relationship('UserLog', backref='user')

    def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.email}>'