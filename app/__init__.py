"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaaahbhp8u791gt3t1g-a.oregon-postgres.render.com",
        database="todoapp_1wra",
        user="todoapp_1wra_user",
        password="RfhtludHQESwz5be5BU7hwRHdzSf9Jbo")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
