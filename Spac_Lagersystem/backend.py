import os
import psycopg


class Database:
    def __init__(self,conn):
        self.conn = conn

    def read(self, query, params=None):
        with self.conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchall()
        
        def write(self, query, params=None):
            with self.conn.cursor() as cur:
                cur.execute(query, params)

# ================ Program setup ================
if __name__ == "__main__":
    db_name = os.environ["DB_NAME"]
    db_user = os.environ["DB_USER"]
    db_pw   = os.environ["DB_PASSWORD"]
    db_host = os.environ["DB_HOST"]

    conn_str =    f"dbname   = {db_name} \
                    user     = {db_user} \
                    host     = {db_host} \
                    password = {db_pw}"

    # Connect to an existing database
    with psycopg.connect(conn_str) as conn:

        db = Database(conn)
        # Now we cean read with write from the database

        # ================ Main loop ================
        while True:
            inp_raw = "DO nothing"
            # Hold up a minute... There was something about having to do HTTP

            [op, query] = inp_raw.split(" ")

            match op:
                case "GET":
                    response = db.read(query)
                    # Do some more
                case "POST":
                    db.write(query)
                    # Do some more?
                case "PUT":
                    print("PUT operation not implemented yet")
                    # Do something
                case "DELETE":
                    print("DELETE operation not implemented yet")
                    # Do something
            
            conn.commit()

        




    # Old code
    """

    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abc'def"))

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM test")
        print(cur.fetchone())
        # will print (1, 100, "abc'def")

        # You can use `cur.executemany()` to perform an operation in batch
        cur.executemany(
            "INSERT INTO test (num) values (%s)",
            [(33,), (66,), (99,)])

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        cur.execute("SELECT id, num FROM test order by num")
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
    """