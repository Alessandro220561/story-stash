from config import db
from sqlalchemy_serializer import SerializerMixin

class UserLog(db.Model, SerializerMixin):
    __tablename__ = 'user_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reading_log_id = db.Column(db.Integer, db.ForeignKey('reading_logs.id'), nullable=False)
    favorite = db.Column(db.Boolean) #user submittable attribute

    def __repr__(self):
        return f'User Log {self.id}, {self.user_id}, {self.reading_log_id}, {self.favorite}'