import json
from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

store_items_URL = "http://localhost:5001/store_items/2"
groupbuy_tracking_URL = "http://localhost:5000/gb_tracking/item/1"


@app.route("/retrieve_items")
def retrieve_items():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            items = request.get_json()
            print("\nReceived an items in JSON:", items)

            # do the actual work
            # 1. Send items {item_id}
            result = processRetrieveProducts(items)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "retrieve_products.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processRetrieveProducts(items):
    # 2. Send the items info {cart items}
    # Invoke the items microservice
    print('\n-----Invoking items microservice-----')
    items_result = invoke_http(store_items_URL, method='GET', json=items)
    print('items_result:', items_result)

    # 4. Record new items
    # record the activity log anyway
    print('\n-----Invoking activity log microservice-----')
    num_groupbuys = invoke_http(groupbuy_tracking_URL, method='GET', json=items_result)
    print("\nitems sent to activity log.\n")
    # - reply from the invocation is not used;
    # continue even if this invocation fails



    # 7. Return created items, shipping record
    return {
        "code": 201,
        "data": {
            "items_result": items_result,
            "groupbuys_result": num_groupbuys
        }
    }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for placing an items...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
