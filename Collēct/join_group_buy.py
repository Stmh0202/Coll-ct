from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

store_items_URL = "http://127.0.0.1:5000/storeitems"
order_URL = "http://127.0.0.1:5001/order"
group_by_tracking_URL = "http://127.0.0.1:5002/gb_tracking"
customer_URL = "http://127.0.0.1:5003/customer/<string:cid>"
seller_URL = "http://127.0.0.1:5004/store"


@app.route("/create_group_buy", methods=['POST']) #post into groupbuy tracking
def create_group_buy():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            groupbuy_details = request.get_json() #groupbuy_details has itemid, cid and sid(to be added)
            print("\nReceived new GroupBuy in JSON:", groupbuy_details)

            # do the actual work
            # 1. Send order info {cart items}
            result = processCreateGB(groupbuy_details)
            # return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "join_group_buy.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processCreateGB(gb_details):
    # 2. Send the order info {cart items}
    # Invoke the store items microservice
    print('\n-----Invoking store items microservice-----')
    item_id = gb_details['itemID'] #maybe might hav to add jsonify
    item_id_json = {"itemId":item_id}
    print(item_id)

    storeitem_result = invoke_http(store_items_URL, method='GET', json=item_id_json)
    item_qty =storeitem_result['data']['items'][0]['itemQty']
    item_quota = storeitem_result['data']['items'][0]['quota']
    print(item_qty,item_quota)
    
    if item_quota > item_qty:
          return "Insufficient Item quantity in the warehouse to fulfill the group buy quota"
    else:
        print('success')
        # update the itemqty in store items micoservice by itemqty - quota


        #create functon to create grpbuyid 
        #invoke grp buy tracking




    
    # 4. Record new order
    # record the activity log anyway
    # print('\n\n-----Invoking activity_log microservice-----')
    # invoke_http(activity_log_URL, method="POST", json=order_result)
    # print("\nOrder sent to activity log.\n")
    # - reply from the invocation is not used;
    # continue even if this invocation fails

    # # Check the order result; if a failure, send it to the error microservice.
    # code = storeitem_result["code"]
    # if code not in range(200, 300):

    #     # # Inform the error microservice
    #     # print('\n\n-----Invoking error microservice as store_item fails-----')
    #     # invoke_http(error_URL, method="POST", json=order_result)
    #     # # - reply from the invocation is not used; 
    #     # # continue even if this invocation fails
    #     # print("Order status ({:d}) sent to the error microservice:".format(
    #     #     code), order_result)

    #     # 7. Return error
    #     return {
    #         "code": 500,
    #         "data": {"store_items_result": storeitem_result},
    #         "message": "Invoking store items failure "
    #     }

   
     
    # print("shipping_result:", shipping_result, '\n')


#def create_gb_id():
    # write some randomising code o create gbId
 


    # # 5. Send new order to shipping
    # # Invoke the shipping record microservice
    # print('\n\n-----Invoking shipping_record microservice-----')
    # shipping_result = invoke_http(
    #     shipping_record_URL, method="POST", json=order_result['data'])
    # print("shipping_result:", shipping_result, '\n')

    # # Check the shipping result; 
    # # if a failure, send it to the error microservice.
    # code = shipping_result["code"]
    # if code not in range(200, 300):

    #     # Inform the error microservice
    #     print('\n\n-----Invoking error microservice as shipping fails-----')
    #     invoke_http(error_URL, method="POST", json=shipping_result)
    #     print("Shipping status ({:d}) sent to the error microservice:".format(
    #         code), shipping_result)

    #     # 7. Return error
    #     return {
    #         "code": 400,
    #         "data": {
    #             "order_result": order_result,
    #             "shipping_result": shipping_result
    #         },
    #         "message": "Simulated shipping record error sent for error handling."
    #     }

    # # 7. Return created order, shipping record
    # return {
    #     "code": 201,
    #     "data": {
    #         "order_result": order_result,
    #         "shipping_result": shipping_result
    #     }
    # }

    # if 


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)