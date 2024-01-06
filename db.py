# db.py

import pyodbc

def get_db_connection():
    connection_string = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-LN60GRJ\\SQLEXPRESS;"  # Ensure the server name matches exactly as in your SQL Server Configuration
        "Database=CourierDB;"  # Replace with the actual name of your database
        "Trusted_Connection=yes;"  # Uses Windows Authentication
    )
    return pyodbc.connect(connection_string)
