from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Replace these values with your actual database credentials
db_config = {
    'user': 'root@localhost',
    'password': 'Shab###0603',
    'host': 'lenovo',
    'database': 'registration_form_db'
}

def connect_to_database():
    """Connects to the database and returns a connection object."""
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/')
def index():
    """Renders the registration form."""
    return render_template('registration.html')

@app.route('/submit-registration', methods=['POST'])
def register():
    """Handles form submission and inserts data into the database."""
    if request.method == 'POST':
        # Get form data
        username = request.form['name']
        email = request.form['email']
        state_of_residence = request.form['state']
        city = request.form['city']
        phone = request.form['phone']
        address = request.form['Address']

        # Connect to database
        connection = connect_to_database()
        if connection:
            try:
                # Create cursor object
                cursor = connection.cursor()

                # Execute SQL query to insert data into database
                query = "INSERT INTO registration (username, email, state_of_residence, city, phone, address) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (username, email, state_of_residence, city, phone, address)
                cursor.execute(query, values)

                # Commit changes
                connection.commit()

                # Close cursor and connection
                cursor.close()
                connection.close()

                # Return a response
                return "Registration successful! Data has been inserted into the database."
            except Exception as e:
                # Rollback changes if there's an error
                connection.rollback()
                return f"Error inserting data into database: {str(e)}"
        else:
            return "Error connecting to the database. Registration failed."

        # For this example, let's just print the data
        print(f"Username: {username}, Email: {email}, State: {state_of_residence}, City: {city}, Phone: {phone}, Address: {address}")

        # Return a response
        return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)