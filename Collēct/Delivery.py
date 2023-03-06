import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3308/delivery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Delivery(db.Model):
    __tablename__ = 'delivery_records'

    delivery_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    Location = db.Column(db.String(100), nullable=False)
    delivery_status = db.Column(db.String(20),nullable=False)
    load_type = db.Column(db.String(20), nullable=False)

    def __init__(self, delivery_id, order_id, Location, delivery_status,load_type):
        self.delivery_id = delivery_id
        self.order_id = order_id
        self.Location = Location
        self.delivery_status = delivery_status
        self.load_type = load_type

    def json(self):
        return {"DeliveryID": self.delivery_id, "OrderID": self.order_id, "Location": self.Location, "DeliveryStatus": self.delivery_status, "LoadType": self.load_type}


@app.route("/deliveryrecords")
def get_all():
    deliverylist = Delivery.query.all()
    if len(deliverylist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "DeliveryRecords": [delivery_records.json() for delivery_records in deliverylist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no delivery records"
        }
    ), 404

@app.route("/deliveryrecords/<string:delivery_id>")
def find_by_isbn13(delivery_id):
    deliveryrecord = Delivery.query.filter_by(delivery_id=delivery_id).first()
    if deliveryrecord:
        return jsonify(
            {
                "code": 200,
                "data": deliveryrecord.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Book not found."
        }
    ), 404

@app.route("/deliveryrecords/<string:deliveryid>", methods=['POST'])
def create_delivery_record(deliveryid):
    if (Delivery.query.filter_by(delivery_id = deliveryid).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Delivery_id": deliveryid
                },
                "message": "Delivery Record already exists"
            }
        ), 400

    data = request.get_json()
    deliveryrecord = Delivery(deliveryid, **data)

    try:
        db.session.add(deliveryrecord)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Delivery_id": deliveryid
                },
                "message": "An error occurred creating the delivery record."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": deliveryrecord.json()
        }
    ), 201



if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
