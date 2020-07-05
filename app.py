from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


def get_data():  # get data every time you request so it's updated
    file = open('./data/stocks.json', 'r')
    data = json.load(file)
    # file.close()
    return data


def get_new_user_id():
    file = open('./data/user.json', 'r')
    data = json.load(file)
    # file.close()
    latest_id = data[-1]['userID']
    return latest_id + 1


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


@app.route('/register')
def register():
    if 'username' not in request.args or 'password' not in request.args:
        return "invalid"
    username = request.args['username']
    password = request.args['password']
    user_id = get_new_user_id()
    data = [{
        'userID': user_id,
        'username': username,
        'password': password,
    }]
    json.dump(data, open('./data/user.json', 'w'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
#
