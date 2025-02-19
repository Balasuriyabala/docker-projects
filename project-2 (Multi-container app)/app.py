import psycopg2
from flask import Flask

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        dbname="mydb",
        user="user",
        password="password",  # Fixed typo here
        host="db"
    )

@app.route("/")
def home():
    conn = connect_db()  # Fixed function call
    conn.close()  # Best practice: Close the connec
