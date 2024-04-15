import logging
from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Function to check if the username and password are valid
def authenticate(username, password):
    try:
        df = pd.read_excel('users.xlsx')
        user_data = df.loc[df['Username'] == username]
        if not user_data.empty and user_data['Password'].iloc[0] == password:
            logging.info("User authenticated successfully: %s", username)
            return True  # Valid username and password
        else:
            logging.warning("Invalid credentials for user: %s", username)
            return False  # Invalid credentials
    except Exception as e:
        logging.error("Error authenticating user: %s", e)
        return False  # Error during authentication

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']

        # Perform authentication
        if authenticate(username, password):
            # If authentication is successful, redirect the user to rough.html
            return redirect('rough.html')
        else:
            # If authentication fails, render the login form again with an error message
            return render_template('login.html', message='Invalid username or password.')
    else:
        # If it's a GET request, render the login form
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
