from flask import Flask, json, request, jsonify, send_file, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3308/store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)
class Store(db.Model):
    __tablename__ = 'store'

    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    address = db.Column(db.String(200),nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    area = db.Column(db.String(20), nullable=False)
    photo = db.Column(db.Text, nullable=False)
    operating_hours = db.Column(db.String(200), nullable=False)
    
    
    def __init__(self, sid, name, description, address, phone, area, photo, operating_hours):
        self.sid = sid
        self.name = name
        self.description = description
        self.address = address
        self.phone = phone
        self.area = area
        self.photo = photo
        self.operating_hours = operating_hours


    def json(self):
        return {"sid": self.sid, "Name": self.name, "Description": self.description, "Address": self.address, "Phone": self.phone, "Area": self.area, "Photo": self.photo, "Operating Hours": self.operating_hours}


@app.route("/store")
def get_all():
    store_list = Store.query.all()
    if len(store_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Stores": [store.json() for store in store_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No stores found"
        }
    ), 404

@app.route("/store/<string:sid>")
def findStore(sid):
    store = Store.query.filter_by(sid=sid).first()
    if store:
        return jsonify(
            {
                "code": 200,
                "data": store.json()
                }
        )
        
    return jsonify(
        {
            "code": 404,
            "message": "Store not found"
        }
    ), 404


if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000, debug=True)
