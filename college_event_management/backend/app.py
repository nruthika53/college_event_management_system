from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        student_name = request.form["student_name"]
        usn = request.form["usn"]
        email = request.form["email"]
        department = request.form["department"]

        db = get_db_connection()
        cursor = db.cursor()

        sql = """
        INSERT INTO students
        (student_name, usn, email, department)
        VALUES (%s, %s, %s, %s)
        """

        values = (student_name, usn, email, department)

        cursor.execute(sql, values)
        db.commit()

        cursor.close()
        db.close()

        return "Registration Successful!"
    
    return render_template("register.html")

    

@app.route("/students")
def students():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("student.html", students=students)

@app.route("/events")
def events():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("events.html", events=events)

@app.route("/event_register", methods=["GET", "POST"])
def event_register():
    if request.method == "POST":
        student_id = request.form["student_id"]
        event_id = request.form["event_id"]

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO event_registrations (student_id, event_id) VALUES (%s, %s)",
            (student_id, event_id)
        )

        db.commit()
        cursor.close()
        db.close()

        return "Event Registration Successful!"

    return render_template("event_register.html")

@app.route("/registrations")
def view_registrations():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            event_registrations.registration_id,
            students.student_name,
            students.usn,
            events.event_name,
            events.event_date
        FROM event_registrations
        JOIN students
            ON event_registrations.student_id = students.id
        JOIN events
            ON event_registrations.event_id = events.event_id
    """)

    registrations = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "registrations.html",
        registrations=registrations
    ) 


if __name__ == "__main__":
    app.run(debug=True)