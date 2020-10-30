from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/') # route
def hello_world(): # route handler
    return 'Hello, World!' # response

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/accounts/<int:accountnumber>', methods=['GET', 'POST', 'PUT'])
def accounts(accountnumber):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'POST':
        pass
    else:
        pass

    return f'Account {accountnumber + 1}'
