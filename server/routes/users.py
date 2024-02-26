from flask_restful import Resource
from models.models import User
from config import api

class Users(Resource):

    def get(self):
        users = [user.to_dict for user in User.query.all()]
        return users, 200