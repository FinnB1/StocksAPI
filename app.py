import os

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def get_data():  # get data every time you request so it's updated
    file = open('./data/stocks.json', 'r')
    data = json.load(file)
    # file.close()
    return data


def get_new_user_id():
    if os.path.isfile('./data/user.json'):
        with open('./data/user.json') as f:
            data = json.load(f)
            return data[len(data)-1][0]['userID'] + 1
    else:
        return 0


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/stocks/getall')
def get_all_stocks():
    response = jsonify(get_data())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/stocks/get')
def get_stock():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return get_all_stocks()

    for stock in get_data():
        if stock['id'] == id:
            return jsonify(stock)


@app.route('/stocks/value')
def get_stock_value():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "argument required"

    for stock in get_data():
        if stock['id'] == id:
            return str(stock['value'])


@app.route('/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    elif request.method == "POST":
        print(request.json['username'])
        if 'username' not in request.json or 'password' not in request.json or 'email' not in request.json:
            return "invalid"
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        user_id = get_new_user_id()
        data = [{
            'userID': user_id,
            'username': username,
            'email': email,
            'password': password,
        }]
        a = []
        if not os.path.isfile('./data/user.json'):
            a.append(data)
            with open('./data/user.json', mode='w') as f:
                f.write(json.dumps(a, indent=1))
        else:
            with open('./data/user.json') as f:
                jsonObject = json.load(f)

            jsonObject.append(data)
            with open('./data/user.json', mode='w') as f:
                f.write(json.dumps(jsonObject, indent=1))
        response = jsonify("Success")
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


if __name__ == '__main__':
    app.run(port=5000)
#
