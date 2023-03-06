import mimetypes
import os
from flask import Flask, request, jsonify, send_file, Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = './uploads'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/storeitems'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



db = SQLAlchemy(app)

class StoreItems(db.Model):
    __tablename__ = 'storeItems'

    sid = db.Column(db.Integer, primary_key=True)
    itemId = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(100), nullable=False)
    itemQty = db.Column(db.Integer, nullable=False)
    # itemImage to check for varbinary
    itemImage = db.Column(db.Text, nullable=False) 
    discountedPrice = db.Column(db.Float(precision=2), nullable=False)
    discountPriceQty = db.Column(db.Integer, nullable=False)
    originalPrice = db.Column(db.Float(precision=2), nullable=False)
    quota = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200),nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

    def __init__(self, sid, itemId, itemName, itemQty, itemImage, discountedPrice, discountPriceQty, originalPrice, quota, category, description, mimetype):
        self.sid = sid
        self.itemID = itemId
        self.itemName = itemName
        self.itemQty = itemQty
        self.itemImage = itemImage
        self.discountedPrice = discountedPrice
        self.discountPriceQty = discountPriceQty
        self.originalPrice = originalPrice
        self.quota = quota
        self.category = category
        self.description = description
        self.mimetype = mimetype

    def json(self):
        return {"sid": self.sid, "itemId": self.itemId, "itemName": self.itemName, "itemQty": self.itemQty, "itemImage": self.itemImage, "discountedPrice": self.discountedPrice, "discountPriceQty": self.discountPriceQty, "originalPrice": self.originalPrice, "quota": self.quota, "category": self.category, "description": self.description, "mimetype":self.mimetype}


@app.route("/storeitems")
def get_all():
    storeItemList = StoreItems.query.all()
    if len(storeItemList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "items": [item.json() for item in storeItemList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no items."
        }
    ), 404


@app.route('/upload',methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded', 400
    
    filename = secure_filename(pic.filename)
    mimetype=pic.mimetype
    save_in_folder_as = f"hello_{filename}"
    pic.save(os.path.join(app.config['UPLOAD_FOLDER'],
            save_in_folder_as))
    newItem = StoreItems(sid=2, itemId=4, itemName=filename, itemQty=2, itemImage=save_in_folder_as, discountedPrice=10.5, discountPriceQty=2, originalPrice=13.5, quota=5, category="food", description="Bigbagelll",  mimetype=mimetype)
    db.session.add(newItem)
    db.session.commit()

    # newItem.itemImage = save_in_folder_as
    # db.session.commit()
    # mimetype = pic.mimetype
    # newItem = StoreItems(sid=1, itemId=2, itemName=filename, itemQty=2, itemImage=pic.read(), discountedPrice=10.5, discountPriceQty=2, originalPrice=13.5, quota=5, category="food", description="Food that is very nice",  mimetype=mimetype)
    # db.session.add(newItem)
    # db.session.commit()
    return 'Image uploaded', 200


# @app.route('/<int:itemId>')
# def get_img(itemId):
#     img = StoreItems.query.filter_by(itemId=itemId).first()
#     if not img:
#         return 'Img Not Found!', 404
    
#     return Response(img.itemImage, mimetype=img.mimetype)

@app.route('/<int:itemId>')
def get_img(itemId):
    img = StoreItems.query.filter_by(itemId=itemId).first()
    pict_path = f'{UPLOAD_FOLDER}/{img.itemImage}'
    return(send_file(pict_path, mimetype=img.mimetype))

if __name__ == '__main__':
<<<<<<< Updated upstream
    app.run(port=5001, debug=True)
=======
    app.run(port=5000, debug=True)
>>>>>>> Stashed changes
