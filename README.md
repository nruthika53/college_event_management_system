College Event Management System

About the Project

The College Event Management System is a beginner-level web application developed to manage college events and student registrations.

It allows students to register, view college events, and register for events. The system stores student details, event information, and registration details in a MySQL database.

Technologies Used

* Python
* Flask
* HTML
* CSS
* MySQL
* MySQL Workbench
* Visual Studio Code

Features

1. Student Registration
2. View Student Details
3. View College Events
4. Register for an Event
5. View Event Registrations
6. MySQL Database Connectivity

Database

Database Name: college_event_db

Tables:

* students
* events
* event_registrations

Project Structure

college_event_management/
│
└── backend/
    ├── app.py
    ├── templates/
    │   ├── index.html
    │   ├── register.html
    │   ├── student.html
    │   ├── events.html
    │   ├── event_register.html
    │   └── registrations.html
    │
    └── static/
        └── style.css

How to Run the Project

1. Install Python.
2. Install the required Python packages:
    pip install flask mysql-connector-python
3. Create the MySQL database named college_event_db.
4. Create the required database tables.
5. Configure your MySQL connection details securely.
6. Open the project folder in VS Code.
7. Run the application:
    python backend/app.py
8. Open your browser and visit:
    http://127.0.0.1:5000/

Project Purpose

This project was developed as a beginner-level college project to learn Python Flask, HTML, CSS, and MySQL database connectivity.
