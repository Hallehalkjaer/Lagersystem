# save this as app.py
import os
import psycopg
from flask import Flask
import backend as be

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

