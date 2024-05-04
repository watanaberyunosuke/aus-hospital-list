from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_FLASK_URL')

db = SQLAlchemy(app)

class Hospital(db.Model):
    __tablename__ = 'Australia_Hospital'
    objectid = db.Column(db.Integer)
    hsib_id = db.Column(db.Integer, primary_key=True)
    hosp_name = db.Column(db.String)
    category = db.Column(db.String)
    street = db.Column(db.String)
    pcode = db.Column(db.String)
    suburb = db.Column(db.String)
    state = db.Column(db.String)
    xcoord = db.Column(db.String)
    ycoord = db.Column(db.String)
    globalid = db.Column(db.String)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/v1/hospital')
def hospital():
# Query the database
    hospitals = Hospital.query.all()

    # Format the data
    formatted_hospitals = []
    for hospital in hospitals:
        hospital_data = {
            'objectid': hospital.objectid,
            'hsib_id': hospital.hsib_id,
            'hosp_name': hospital.hosp_name,
            'category': hospital.category,
            'street': hospital.street,
            'pcode': hospital.pcode,
            'suburb': hospital.suburb,
            'state': hospital.state,
            'xcoord': hospital.xcoord,
            'ycoord': hospital.ycoord,
            'globalid': hospital.globalid
        }
        formatted_hospitals.append(hospital_data)

    # Return JSON
    return jsonify(formatted_hospitals)

if __name__ == '__main__':
    app.run(debug=True)