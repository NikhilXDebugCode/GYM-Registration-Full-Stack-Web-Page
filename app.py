from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DB_NAME = "gym.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            height REAL,
            weight REAL,
            membership_plan TEXT NOT NULL,
            goal TEXT NOT NULL,
            experience_level TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = (
            request.form.get("full_name"),
            request.form.get("email"),
            request.form.get("phone"),
            request.form.get("age"),
            request.form.get("gender"),
            request.form.get("height"),
            request.form.get("weight"),
            request.form.get("membership_plan"),
            request.form.get("goal"),
            request.form.get("experience_level")
        )

        # Validation – NO EMPTY VALUES
        if None in data or "" in data:
            return "All fields are required", 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO members
            (full_name, email, phone, age, gender, height, weight, membership_plan, goal, experience_level)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        conn.close()

        return render_template("success.html", name=data[0])

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
