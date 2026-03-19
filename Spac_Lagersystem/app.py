# save this as app.py
import os
from psycopg_pool import ConnectionPool
from flask import Flask, g, jsonify, request, send_from_directory

class Database:
    def __init__(self,conn):
        self.conn = conn

    def get_filtered_data(self, lower_bound, upper_bound):
        with self.conn.cursor() as cur:
            return 0
            #cur.execute()

    def get_all_data(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM Lager")
            data = cur.fetchall()
            return data



    def read(self, query, params=None):
        with self.conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchall()
        
    def write(self, query, params=None):
        with self.conn.cursor() as cur:
            cur.execute(query, params)


app = Flask(__name__)


"""
DB has columns:
    ProductID               serial PRIMARY KEY
    ProductName             varchar[255]
    ProductStockQuantity    integer
    ProductLocation         varchar[255]
    ProductStatus           varchar[255]

"""

db_name = os.environ["DB_NAME"]
db_user = os.environ["DB_USER"]
db_pw   = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]

conn_str =    f"dbname   = {db_name} \
                user     = {db_user} \
                host     = {db_host} \
                password = {db_pw}"

#os.system("echo "+conn_str)

pool = ConnectionPool(conn_str)
#conn = psycopg.connect(conn_str)

# A way of getting the database within the context of the event handlers
def get_db():
    if "db" not in g:
        conn = pool.getconn()
        g.db = Database(conn)
        g._conn = conn
    return g.db

# Close connection to db when app closes
@app.teardown_appcontext
def close_db(exception):        
    conn = g.pop("_conn", None)
    if conn is not None:
        pool.putconn(conn)



# Serves the CSS styling and the homepage images etc.
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)

# Serves the HTML in the homepage
@app.route("/")
def homepage():
    return send_from_directory("static", "index.html")

# Event handler for the "add" button
@app.route("/add_smth")
def get_something():
    db = get_db()
    data = db.get_all_data()
    print(data)
    return data

@app.route("/loadProducts")
def loadProducts():
    db = get_db()
    data = db.get_all_data()
    return data

# These two event handlers should be swapped. This is just for testing
@app.route("/get_smth")
def add_something():

    #os.system("echo Python sees that the button has been pressed")
    #query = "INSERT INTO test (ProductName, ProductStockQuantity, ProductLocation, ProductStatus) \
    #                VALUES (%(ProductName)s, %(ProductStockQuantity)s, %(ProductLocation)s, %(ProductStatus)s);"
    param_dict = {  #"Name":       "Dette er en test",
                    #"Stock":      45,
                    #"Location":   "Ballerup",
                    "Status":      "OK"
                    }
    query = "smth"



    with conn.cursor() as cur:
        # This works:
        # "INSERT INTO test (ProductStockQuantity) VALUES (%s);", [45,]
        cur.execute("INSERT INTO Lager (ProductStatus) VALUES (%s);", ("OK",))
    
    
    
    #query = "INSERT INTO test (ProductID, ProductName, ProductStockQuantity, ProductLocation, ProductStatus) VALUES (420, \"Hejsa\", 69, \"Ballerup\", \"OK\")"
    #out = db.write(query, ("ok"))
    return "return string"
    """
    with conn.cursor() as cur:
        cur.execute("POST TO test ")
        record = cur.fetchone()
        return record[0].isoformat()
    """

@app.route("/addProduct", methods=["POST"])
def addProduct():
    db = get_db()
    data = request.get_json()
    with db.conn.cursor() as cur:
        cur.execute(
            "INSERT INTO Lager (ProductName, ProductID, ProductStockQuantity, ProductLocation) VALUES (%s, %s, %s, %s)",
            (data["navn"], data["sku"], data["lager"], data["lokation"])
        )
        db.conn.commit()
    return "Tilføjet", 200

@app.route("/deleteProduct/<int:product_id>", methods=["DELETE"])
def deleteProduct(product_id):
    db = get_db()
    with db.conn.cursor() as cur:
        cur.execute("DELETE FROM Lager WHERE ProductID = %s", (product_id,))
        db.conn.commit()
    return "Deleted", 200







"""
#dummy data used for testing
books = [
    {"id": 1, "title": "Concept of Physics", "author": "H.C Verma"},
    {"id": 2, "title": "Gunahon ka Devta", "author": "Dharamvir Bharti"},
    {"id": 3, "title": "Problems in General Physsics", "author": "I.E Irodov"}
]

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

"""



if __name__ == "__main__":
    app.run(host='0.0.0.0')

