import flask
from flask import request
from inventory.services.handler import inventory_info_handler
import logging

app = flask.Flask(__name__)

logging.basicConfig(filename='services.log', encoding='utf-8', level=logging.DEBUG)


@app.route('/getproductdetails', methods=['GET'])
def get_product_details():
    logging.info('jkjj')
    response = inventory_info_handler.InventoryHandler().get_product_details()
    logging.info("get response: %s", response)
    return response


@app.route('/insertproductdetails', methods=['POST'])
def insert_product_details():
    params = request.get_json()
    logging.info("inside api")
    product_name = params['product_name']
    quantity = params['quantity']
    return inventory_info_handler.InventoryHandler().insert_product_details(product_name, quantity)


@app.route('/deleteproductdetails', methods=['POST'])
def delete_product_details():
    params = request.get_json()
    logging.info("inside delete api")
    productId = params['productId']
    return inventory_info_handler.InventoryHandler().delete_product_details(productId)


@app.route('/getlocationdetails', methods=['GET'])
def get_location_details():
    logging.info('jkjj')
    response = inventory_info_handler.InventoryHandler().get_location_details()
    logging.info("get response: %s", response)
    return response


@app.route('/insertlocationdetails', methods=['POST'])
def insert_location_details():
    params = request.get_json()
    logging.info("inside api")
    location_name = params['location_name']
    return inventory_info_handler.InventoryHandler().insert_location_details(location_name)


@app.route('/deletelocationdetails', methods=['POST'])
def delete_location_details():
    params = request.get_json()
    logging.info("inside delete api")
    locationId = params['locationId']
    return inventory_info_handler.InventoryHandler().delete_location_details(locationId)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
