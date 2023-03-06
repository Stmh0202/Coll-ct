from flask import Flask, request, jsonify, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/customer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
class customer(db.Model):
    __tablename__ = 'customer'
 
    cid = db.Column(db.String(10), primary_key=True)
    name = db.Column (db.String(64), nullable=False)
    address = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64),nullable=False)
    password = db.Column(db.String(64), nullable=False)
 
    def __init__(self, cid, name, address, phone, email, password):
        self.cid= cid
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email 
        self.password = password 

    def json(self):
        return {"cid": self.cid, "name": self.name, "address": self.address, "phone": self.phone,"email": self.email,"password": self.password}
 
 # do we wanna do like GET/cid/address , GET/cid/phone for each detail?
@app.route("/customer/<string:cid>")
def find_by_cid(cid):
    customer_details = customer.query.filter_by(cid=cid).first()
    if customer_details:
        return jsonify (
            {
                "code": 200,
                "data": customer_details.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    this_user = customer.query.filter_by(email=email).first()

    # Email not found in DB
    if this_user == None:
        output = (jsonify(code = 404), 404)
        return output
    
    # Password entered does not match DB's password
    if password != this_user.password:
        output = (jsonify(code = 401), 401)
        return output

    # Login success
    output = (jsonify(code = 200, body = {'user_id': this_user.cid}), 200)
    return redirect("http://localhost/ESD-Project/index.html", 301)


#     if cust_details:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "details": [detail.json() for detail in cust_details]
#                 }
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "Customer not found."
#         }
#     ), 404
 
 
# # @app.route("/book/<string:isbn13>")
# # def find_by_isbn13(isbn13):
# #     book = Book.query.filter_by(isbn13=isbn13).first()
# #     if book:
# #         return jsonify(
# #             {
# #                 "code": 200,
# #                 "data": book.json()
# #             }
# #         )
# #     return jsonify(
# #         {
# #             "code": 404,
# #             "message": "Book not found."
# #         }
# #     ), 404
 
 
# # @app.route("/book/<string:isbn13>", methods=['POST'])
# # def create_book(isbn13):
# #     if (Book.query.filter_by(isbn13=isbn13).first()):
# #         return jsonify(
# #             {
# #                 "code": 400,
# #                 "data": {
# #                     "isbn13": isbn13
# #                 },
# #                 "message": "Book already exists."
# #             }
# #         ), 400
 
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
#             "data": book.json()
#         }
#     ), 201
 
 
if __name__ == '__main__':
    app.run(port=5000, debug=True) #might need to change the port = 5000 