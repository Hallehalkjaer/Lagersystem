# save this as app.py
import os
from psycopg_pool import ConnectionPool
from flask import Flask, g, jsonify, request, send_from_directory

app = Flask(__name__)


db_name = os.environ["DB_NAME"]
db_user = os.environ["DB_USER"]
db_pw   = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]

conn_str =    f"dbname   = {db_name} \
                user     = {db_user} \
                host     = {db_host} \
                password = {db_pw}"

pool = ConnectionPool(conn_str)

# A way of getting the database within the context of the event handlers
def get_db():
    if "db" not in g:
        conn = pool.getconn()
        g.db = conn
    return g.db

# Close connection to db when app closes
@app.teardown_appcontext
def close_db(exception):        
    conn = g.pop("db", None)
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

# Loads all the products for displaying on the front page
@app.route("/loadProducts")
def loadProducts():
    db = get_db()
    with db.cursor() as cur:
        cur.execute("SELECT * FROM Lager")
        data = cur.fetchall()
    return data

# Add a product to the databse
@app.route("/addProduct", methods=["POST"])
def addProduct():
    db = get_db()
    data = request.get_json()
    with db.cursor() as cur:
        cur.execute(
            "INSERT INTO Lager (ProductName, ProductID, ProductStockQuantity, ProductLocation) VALUES (%s, %s, %s, %s)",
            (data["navn"], data["sku"], data["lager"], data["lokation"])
        )
        db.commit()
    return "Tilføjet", 200

# Delete a product from the database
@app.route("/deleteProduct/<int:product_id>", methods=["DELETE"])
def deleteProduct(product_id):
    db = get_db()
    with db.cursor() as cur:
        cur.execute("DELETE FROM Lager WHERE ProductID = %s", (product_id,))
        db.commit()
    return "Deleted", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')

