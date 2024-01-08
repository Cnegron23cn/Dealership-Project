from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = 'dealership'

class Car:
    def __init__(self, data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.price = data['price']
        self.milage = data['milage']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query= 'SELECT * FROM cars;'
        results = connectToMySQL(db).query_db(query)
        car = []
        for row in results:
            car.append(cls[row])
        return car

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO cars (make, model, price, milage, user_id)
        VALUES (%(make)s, %(model)s, %(price)s, %(milage)s, %(user_id)s);
        """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM cars WHERE id = %(id)s;'
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])