# TO BE EDITED
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3308/gb_tracking'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

CORS(app)
 
class gb_tracking(db.Model):
    __tablename__ = 'gb_tracking'
 
    gbId = db.Column (db.String(64), primary_key=True)
    storeId = db.Column(db.String(64), nullable=False)
    itemId = db.Column(db.String(10), nullable=False)
    quota = db.Column(db.Integer,nullable=False)
    cid = db.Column(db.String(10), primary_key=True)
    timeStamp = db.Column(db.DateTime, nullable=False,
                         default=datetime.now, onupdate=datetime.now)
    numItems = db.Column(db.Integer,nullable=False)
 
    def __init__(self, gbId, storeId, itemId, quota, cid, timeStamp,numItems):
        self.gbId = gbId
        self.storeId = storeId
        self.itemId = itemId
        self.quota = quota
        self.cid = cid 
        self.timeStamp = timeStamp
        self.numItems = numItems

    def json(self):
        return {"gbId": self.gbId, "storeId": self.storeId, "itemId": self.itemId, "cid": self.cid, "quota": self.quota,"timeStamp": self.timeStamp, "numItems":self.numItems}

@app.route("/gb_tracking")
def get_all():
    gbt_details = gb_tracking.query.all()
    if len(gbt_details):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "gbt": [gbt.json() for gbt in gbt_details]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no groupbuy."
        }
    ), 404


@app.route("/gb_tracking/<string:gbId>/<string:cid>")
def find_by_cid(cid, gbId):
    gbt_details = gb_tracking.query.filter_by(cid=cid, gbId=gbId).first()
    if gbt_details:
        return jsonify (
            {
                "code": 200,
                "data": gbt_details.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404


@app.route("/gb_tracking/<string:gbId>")
def get_quota(gbId):
    gb_id_details = gb_tracking.query.filter_by(gbId=gbId).first()
    if gb_id_details:
        return gb_id_details.quota

    return jsonify(
        {
            "code": 404,
            "message": "Can't retrieve details."
        }
    ), 404

 
@app.route("/gb_tracking/<string:gbId>/<string:cid>/<int:numItems>", methods=['POST'])
def create_groupbuy(gbId, cid, numItems):

    gb_details = gb_tracking.query.filter_by(gbId=gbId, cid=cid)
    if (gb_details.first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "gbId": gbId,
                     "cidId": cid
                },
                "message": "group buy track already exists."
            }
        ), 400

    elif (gb_tracking.query.filter_by(gbId=gbId)):
        gb_details = gb_tracking.query.filter_by(gbId=gbId)
        num_of_customers = str((gb_tracking.query.filter_by(gbId=gbId)).count())
        #aggregates all the quantIty of the same gbId
        total_num_of_items = 0
        for cust in gb_details: 
            total_num_of_items += int(cust.numItems)
        
        Quota = get_quota(gbId)

        if (total_num_of_items == Quota): 
            return 'Quota has reached'
        elif (total_num_of_items + numItems > Quota):
            newQty = Quota-total_num_of_items
            return 'Reduce your Quantity to ' + str(newQty)
        else:
            Quota += numItems
    
    data = request.get_json()
    new_gb = gb_tracking(gbId, **data)

    try:
        db.session.add(new_gb)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "gbId": gbId,
                    "cid": cid
                },
                "message": "An error occurred creating the groupbuy tracking."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": new_gb.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(port=5100, debug=True)

# @app.route("/book/<string:isbn13>")
# def find_by_isbn13(isbn13):
#     book = Book.query.filter_by(isbn13=isbn13).first()
#     if book:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": book.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "Book not found."
#         }
#     ), 404
 
 
# @app.route("/book/<string:isbn13>", methods=['POST'])
# def create_book(isbn13):
#     if (Book.query.filter_by(isbn13=isbn13).first()):
#         return jsonify(
#             {
#                 "code": 400,
#                 "data": {
#                     "isbn13": isbn13
#                 },
#                 "message": "Book already exists."
#             }
#         ), 400
 
#     data = request.get_json()
#     book = Book(isbn13, **data)
 
#     try:
#         db.session.add(book)
#         db.session.commit()
#     except:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "isbn13": isbn13
#                 },
#                 "message": "An error occurred creating the book."
#             }
#         ), 500
 
#     return jsonify(
#         {
#             "code": 201,
    #         "data": book.json()
    #     }
    # ), 201
 
 
# @app.route("/gb_tracking/create", methods=['POST'])
# def create_gb_tracking():
#     gb_id = request.json.get('gb_id', None)
#     cid = request.json.get('cid', None)
#     store_id = request.json.get('store_id', None)
#     item_id = request.json.get('item_id', None)
#     quota = request.json.get('quota', None)
#     timestamp = request.json.get('timestamp', None)
#     GB = gb_tracking(cid=cid, gb_id=gb_id, status='NEW')

#     # cart_item = request.json.get('cart_item')
#     # for item in cart_item:
#     #     order.order_item.append(Order_Item(
#     #         book_id=item['book_id'], quantity=item['quantity']))
#     try:
#         db.session.add(GB)
#         db.session.commit()
#     except Exception as e:
#         return jsonify(
#             {
#                 "code": 500,
#                 "message": "An error occurred while creating the groub buy. " + str(e)
#             }
#         ), 500

#     # return jsonify(
#     #     {
#     #         "code": 201,
#     #         "data": GB.json()
#     #     }
#     # ), 201
#     return jsonify(
#         {
#             "code": 201,
#             "data": "it works"
#         }
#     ), 201

 