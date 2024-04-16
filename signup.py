import logging
from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Function to append user data to the Excel file
def write_to_excel(data):
    try:
        # Read existing data from Excel file
        try:
            df = pd.read_excel('users.xlsx')
        except FileNotFoundError:
            # If file doesn't exist, create a new DataFrame
            df = pd.DataFrame(columns=['Username', 'Email', 'Password'])

        # Append new user data to DataFrame
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

        # Write DataFrame back to Excel file
        df.to_excel('users.xlsx', index=False)
        logging.debug("Data written to Excel file successfully.")
    except Exception as e:
        logging.error("Error writing to Excel database:", e)

# Route for the signup form
@app.route('/')
def signup_form():
    return render_template('signup.html')

# Route to handle form submission
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Write user data to the Excel file
    write_to_excel({'Username': username, 'Email': email, 'Password': password})

    # Redirect to login page after successful signup
    return redirect('/login')

# Route for the login page
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)
