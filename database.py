import mysql.connector

def connect_to_database():
    # Establish connection
    connection = mysql.connector.connect(
        host="lenovo",
        user="root@localhost",
        password="Shab###0603",
        database="registration_form_db"
    )
    return connection

def execute_query(connection, query):
    # Create cursor object
    cursor = connection.cursor()

    # Execute SQL query
    cursor.execute(query)

    # Fetch results
    results = cursor.fetchall()

    # Close cursor
    cursor.close()

    return results
