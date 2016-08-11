import pymysql
import dbconfig


class DBHelper:

    def connect(self, database="crimemap"):
        return pymysql.connect(
            host='localhost',
            user=dbconfig.db_user,
            passwd=dbconfig.db_password,
            db=database,
        )

    def add_crime(self, category,  date, latitude, longitude, description):
        pass

    def get_all_crimes(self):
        return[{
            'latitude': -33.301304,
            'longitude': 26.523355,
            'date': '2000-01-01',
            'category': 'mugging'
        }]
