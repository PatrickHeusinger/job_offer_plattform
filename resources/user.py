from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import User

class UserListResource(Resource):

    def post(self):

        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        if User.get_by_username(username=username):
            return {'message': 'username already exists'}, HTTPStatus.BAD_REQUEST

        user = User(
            username=username,
            password=password
        )

        user.save()

        return user.data, HTTPStatus.CREATED
