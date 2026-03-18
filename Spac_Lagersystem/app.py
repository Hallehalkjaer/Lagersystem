# save this as app.py
import os
import psycopg
from flask import Flask, jsonify, request
import backend as be


#dummy data used for testing
books = [
    {"id": 1, "title": "Concept of Physics", "author": "H.C Verma"},
    {"id": 2, "title": "Gunahon ka Devta", "author": "Dharamvir Bharti"},
    {"id": 3, "title": "Problems in General Physsics", "author": "I.E Irodov"}
]

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/books", methods=["GET"])
def GetAllBooks():
    return jsonify(books)

@app.route("/books/<int:book_id>", methods=["GET"])
def GetBookById(book_id):
    return be.GetBookById(book_id)

@app.route("/books", methods=["POST"])
def AddBook():
    num = request.args.get('book_id')
    title = request.args.get('book_title')
    author = request.args.get('book_author')

    return be.AddBook(num, title, author)

@app.route("/books/<int:book_id>", methods=["DELETE"]) 
def DeleteBook():
    num = request.args.get('book_id')
    return be.DeleteBook(num)

@app.route("/books/<int:book_id>", methods=["PUT"])
def UpdateBook():
    num = request.args.get('book_id')
    title = request.args.get('book_title')
    author = request.args.get('book_author')

    return be.UpdateBook(num, title, author)



