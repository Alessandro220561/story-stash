from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String)
    readings = db.relationship('ReadingLog', backref='user')
    user_logs = db.relationship('UserLog', backref='user')

    def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.email}>'

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    genre = db.Column(db.String)
    pages = db.Column(db.Integer)
    readings = db.relationship('ReadingLog', backref='book')

    def __repr__(self):
        return f'<Book {self.id}, {self.title}, {self.author}, {self.genre}, {self.pages}>'
    
class ReadingLog(db.Model, SerializerMixin):
    __tablename__ = 'reading_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    user_logs = db.relationship('UserLogs', backref='readinglog')

    def __repr__(self):
        return f'Reading Log {self.id}, {self.user_id}, {self.book_id}, {self.start_date}, {self.end_date}'
    
class UserLog(db.Model, SerializerMixin):
    __tablename__ = 'user_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reading_log_id = db.Column(db.Integer, db.ForeignKey('reading_logs.id'), nullable=False)
    favorite = db.Column(db.Boolean) #user submittable attribute

    def __repr__(self):
        return f'User Log {self.id}, {self.user_id}, {self.reading_log_id}, {self.favorite}'

