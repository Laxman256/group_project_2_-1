from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


def fetch_hotel_data():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM hotel_data')
    columns = [col[0] for col in cursor.description]  # Get column names
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]  # Convert rows to dictionaries
    con.close()
    return data

@app.route('/')
def home():
    return render_template("home.html")

# Route to display the hotel data
@app.route('/view_data.html')
def view_data():
    return render_template("view_data.html", hotel_data=fetch_hotel_data)



@app.route('/about.html')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
