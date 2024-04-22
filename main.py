from flask import Flask, render_template, request
from database import connect_to_database  # Import the function here

app = Flask(__name__)

# Define your routes and other functions here...

from database import connect_to_database, execute_query

# Establish connection
connection = connect_to_database()

# Execute query
query = "SELECT * FROM registration"
results = execute_query(connection, query)

# Print results
for row in results:
    print(row)

# Close connection
connection.close()
