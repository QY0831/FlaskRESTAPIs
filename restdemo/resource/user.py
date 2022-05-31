from flask_restful import Resource, reqparse

user_list = []


def min_length_str(min_length):
    def validate(s):
        if not s:
            raise Exception('password required')
        if not isinstance(s, (int, str)):
            raise Exception('password format error')
        s = str(s)
        if len(s) >= min_length:
            return s
        raise Exception("String must be at least %i long" % min_length)

    return validate


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password', type=min_length_str(5), required=True,
        help='{error_msg}'
    )

    def get(self, username):
        for user in user_list:
            if user['username'] == username:
                return user
        return {'message': 'user not found'}, 404

    def post(self, username):

        User.parser.parse_args()  # filter args
        user = {
            'username': username,
            'password': request.get_json().get('password')
        }
        user_list.append(user)
        return user, 201

    def delete(self, username):
        user_find = None
        for user in user_list:
            if user['username'] == username:
                user_find = user
        if user_find:
            user_list.remove(user_find)
            return user_find
        else:
            return {
                       'message': 'user not found'
                   }, 204

    def put(self, username):
        user_find = None
        for user in user_list:
            if user['username'] == username:
                user_find = user
        if user_find:
            User.parser.parse_args()
            user_list.remove(user_find)
            user_find['password'] = request.get_json()['password']
            user_list.append(user_find)
            return user_find
        else:
            return {
                       'message': 'user not found'
                   }, 204


class UserList(Resource):

    def get(self):
        return user_list