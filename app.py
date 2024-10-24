from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return connection

@app.route('/')
def index():
    return "Hello, Flask!"

@app.route('/data')
def data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sample_table")  # Change this according to your table name
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

