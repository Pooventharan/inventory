from inventory.services.utils import inventory_info_utils

import logging

logging.basicConfig(filename='dao.log', encoding='utf-8', level=logging.DEBUG)


class InventoryDAO(object):
    def __init__(self):
        self.connection = inventory_info_utils.DBConnector().create_connection()

    def get_product_details(self):
        try:
            logging.info('get dao')
            sql = "select * from product"
            cursor = self.connection.cursor()
            cursor.execute(sql, )
            result = cursor.fetchall()
            response = []
            for row in result:
                item = {
                    'productId': row[0],
                    'productName': row[1],
                    'quantity': row[2]
                }
                response.append(item)
            logging.info('response: %s', response)
            return response
        except Exception as e:
            logging.exception(e)

    def insert_product_details(self, product_name, quantity):
        try:
            sql = "insert into product(productName, quantity) values(%s, %s)"
            value = (product_name, quantity)
            cursor = self.connection.cursor()
            cursor.execute(sql, value)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            logging.exception(e)

    def delete_product_details(self, productId):
        try:
            sql = "delete from product where productId = %s"
            value = (productId,)
            cursor = self.connection.cursor()
            cursor.execute(sql, value)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            logging.exception(e)

    def get_location_details(self):
        try:
            logging.info('get dao')
            sql = "select * from location"
            cursor = self.connection.cursor()
            cursor.execute(sql, )
            result = cursor.fetchall()
            response = []
            for row in result:
                item = {
                    'locationId': row[0],
                    'locationName': row[1],
                }
                response.append(item)
            logging.info('response: %s', response)
            return response
        except Exception as e:
            logging.exception(e)

    def insert_location_details(self, location_name):
        try:
            sql = "insert into location(locationName) values(%s)"
            value = (location_name,)
            cursor = self.connection.cursor()
            cursor.execute(sql, value)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            logging.exception(e)

    def delete_location_details(self, locationId):
        try:
            sql = "delete from location where locationId=%s"
            value = (locationId,)
            cursor = self.connection.cursor()
            cursor.execute(sql, value)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            logging.exception(e)
