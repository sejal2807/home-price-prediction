from flask import Flask, request, jsonify, render_template
from util import get_location_names, get_estimated_price


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    estimated_price = get_estimated_price(location,total_sqft,bhk,bath)
    estimated_price = str(round(estimated_price,4)) + " Lakhs"

    return render_template('index.html', response= estimated_price)


if __name__ == "__main__":
    app.run(debug=True)
