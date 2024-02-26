from config import db
from sqlalchemy_serializer import SerializerMixin

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