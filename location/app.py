from flask import Flask , jsonify , request
import json

app = Flask(__name__)

def get_location_names():
    with open ("columns.json",'r') as f:
        data_columns = json.load(f)['data_columns']
        global len_of_columns
        len_of_columns = len(data_columns)
        data_columns = data_columns[3:]
    return data_columns

@app.route('/')
def index():
    return 'welcome to the server'


@app.route('/get_location',methods=['Get'])
def get_location():
    response = jsonify({
        "locations": get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)