from flask import jsonify
from inventory.services.dao import inventory_info_dao
import logging

logging.basicConfig(filename='handler.log', encoding='utf-8', level=logging.DEBUG)


class InventoryHandler(object):
    def __init__(self):
        self.daoObject = inventory_info_dao.InventoryDAO()

    def get_product_details(self):
        return jsonify(self.daoObject.get_product_details())

    def insert_product_details(self, product_name, quantity):
        return jsonify(self.daoObject.insert_product_details(product_name, quantity))

    def delete_product_details(self, productId):
        return jsonify(self.daoObject.delete_product_details(productId))

    def get_location_details(self):
        return jsonify(self.daoObject.get_location_details())

    def insert_location_details(self, location_name):
        return jsonify(self.daoObject.insert_location_details(location_name))

    def delete_location_details(self, locationId):
        return jsonify(self.daoObject.delete_location_details(locationId))
