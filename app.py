from flask import Flask, jsonify


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

stocks = [
    {'id': 1,
     'name': 'Banana',
     'abbrev': 'BANA'},
    {'id': 2,
     'name': 'General Development',
     'abbrev': 'GD'},
    {'id': 3,
     'name': 'Citizen & Sons',
     'abbrev': 'CNS'},
    {'id': 4,
     'name': 'Vista plc',
     'abbrev': 'VSTA'},
    {'id': 5,
     'name': 'Kent',
     'abbrev': 'KENT'},
]

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/stocks/getall')
def get_all_stocks():
    response = jsonify(stocks)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()
#host='0.0.0.0', port=5555