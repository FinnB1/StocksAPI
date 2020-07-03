from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

file = open('./data/stocks.json', 'r')
data = json.load(file)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/stocks/getall')
def get_all_stocks():
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/stocks/get')
def get_stock():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return get_all_stocks()

    for stock in data:
        if stock['id'] == id:
            return jsonify(stock)


@app.route('/stocks/value')
def get_stock_value():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "argument required"

    for stock in data:
        if stock['id'] == id:
            return str(stock['value'])


if __name__ == '__main__':
    app.run()
# host='0.0.0.0', port=5555
