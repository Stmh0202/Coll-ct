
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3308/orders_proj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)


class Order(db.Model):
    __tablename__ = 'orders_proj'

    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    itemName = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    DiscountedQtyPrice = db.Column(db.Float , nullable = False)
    
    def __init__(self, order_id, customer_id, itemName,quantity,DiscountedQtyPrice):
        self.order_id = order_id
        self.customer_id = customer_id
        self.itemName = itemName
        self.quantity = quantity
        self.DiscountedQtyPrice = DiscountedQtyPrice

    def json(self):
        return {"Order ID": self.order_id, "Customer ID": self.customer_id, "item Name": self.itemName, "Quantity": self.quantity, "Discounted Price": self.DiscountedQtyPrice}



@app.route("/order")
def get_all():
    orderlist = Order.query.all()
    if len(orderlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "orders": [order.json() for order in orderlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no orders."
        }
    ), 404


@app.route("/order/<string:order_id>")
def find_by_order_id(order_id):
    order = Order.query.filter_by(order_id=order_id).first()
    if order:
        return jsonify(
            {
                "code": 200,
                "data": order.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "order_id": order_id
            },
            "message": "Order not found."
        }
    ), 404


@app.route("/order", methods=['POST'])
def create_order():
    customer_id = request.json.get('customer_id', None)
    itemName = request.json.get('itemName')
    quantity = request.json.get('quantity')
    DiscountedQtyPrice = request.json.get('DiscountedQtyPrice')
    order = Order(customer_id=customer_id, itemName=itemName,quantity = quantity,DiscountedQtyPrice=DiscountedQtyPrice)
    
    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": order.json()
        }
    ), 201


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5001, debug=True)
