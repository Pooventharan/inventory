import mysql.connector


class DBConnector:
    def create_connection(self):
        con = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="978800@Skp",
            db="inventory"
        )
        return con
