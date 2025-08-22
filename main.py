from flask import Flask, request, jsonify, render_template
import os
from cs50 import SQL


if not os.path.exists("database.db"):
    open("database.db", "w").close()

db = SQL("sqlite:///database.db")
app = Flask(__name__)

db.execute("""
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        inp1 TEXT NOT NULL,
        inp2 TEXT NOT NULL,
        textbox TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")


@app.route('/')
def index():
    user_name = "ANIII"
    return render_template('index.html', user_name=user_name)

@app.route('/submit', methods=['POST'])
def submit():
    inp1 = request.form.get("inp1")
    inp2 = request.form.get("inp2")
    textbox = request.form.get("textbox")

    db.execute("INSERT INTO entries (inp1, inp2, textbox) VALUES (?, ?, ?)", inp1, inp2, textbox)

    return jsonify({"status": "success", "message": "Data inserted successfully!"})


@app.route('/all')
def allview():
    user_name = "idk who you are"
    data = db.execute("SELECT * FROM entries")
    return render_template('all.html', user_name=user_name, data=data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)