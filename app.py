from flask import Flask, jsonify

app = Flask(__name__)

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


@app.route('/stocks/getall', methods=['GET'])
def get_all_stocks():
    return jsonify(stocks)


if __name__ == '__main__':
    app.run()
