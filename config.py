# Database configuration
from flask import Flask

DB_CONFIG = {
    "server": "bmislol\\SQLEXPRESS",  # Replace with your SQL Server hostname or IP
    "database": "Qistify",            # Updated to your actual project database
    "username": "sa",                 # Your SQL Server username
    "password": "78867"               # Your SQL Server password
}

app = Flask(__name__)
app.config["SECRET_KEY"] = "e8c9f2d7b4a1c3e5f8a2d9b3c7e1f4a5"  # Ensure this is kept secure
app.config["SESSION_COOKIE_SECURE"] = False  # Set to True in production with HTTPS
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_PERMANENT"] = True
