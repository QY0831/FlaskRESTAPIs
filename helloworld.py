from flask import Flask, jsonify, request

app = Flask(__name__)

user_list = [
    {
        'username': 'abc',
        'password': 'abc'
    },
    {
        'username': '123',
        'password': '123'
    }
]


@app.route('/')
def helloworld():
    return "hello world"


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(user_list)


@app.route('/user', methods=['POST'])
def create_user():
    user = request.get_json()
    user_check = list(
        filter(
            lambda x: user.get('username') == x['username'],
            user_list
        )
    )
    if user_check:
        return jsonify({
            'message': 'user exist'
        })

    user_list.append(user)
    return jsonify({
        'message': 'user created'
    })


@app.route('/user/<username>', methods=['DELETE', 'PUT'])
def delete_user(username):
    user_find = None
    for user in user_list:
        if user['username'] == username:
            user_find = user
    if not user_find:
        return jsonify({
            'message': 'user not found'
        })
    if request.method == 'DELETE':
        user_list.remove(user_find)
        return jsonify({
            'message': 'user deleted'
        })
    elif request.method == 'PUT':
        new_passwd = request.get_json()["password"]
        user_find["password"] = new_passwd
        return jsonify({
            'message': 'user passwd updated'
        })


if __name__ == '__main__':
    app.run()
