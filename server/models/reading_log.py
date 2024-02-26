from config import db
from sqlalchemy_serializer import SerializerMixin

class ReadingLog(db.Model, SerializerMixin):
    __tablename__ = 'reading_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    user_log = db.relationship('UserLog', backref='readinglog')

    def __repr__(self):
        return f'Reading Log {self.id}, {self.user_id}, {self.book_id}, {self.start_date}, {self.end_date}'