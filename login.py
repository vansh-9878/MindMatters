import logging
from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Function to check if the username and password are valid
# def authenticate(username, password):
#     try:
#         df = pd.read_excel('users.xlsx')
#         user_data = df.loc[df['Username'] == username]
#         if not user_data.empty:
#             if user_data['Password'].iloc[0] == password:
#                 return True  # Valid username and password
#             else:
#                 return 'invalid_password'  # Invalid password
#         else:
#             return 'invalid_username'  # Invalid username
#     except Exception as e:
#         logging.error("Error authenticating user:", e)
#         return 'error'
def authenticate(username, password):
    try:
        df = pd.read_excel('users.xlsx')
        user_data = df.loc[df['Username'] == username]
        if not user_data.empty:
            if user_data['Password'].iloc[0] == password:
                logging.info("User authenticated successfully: %s", username)
                return True  # Valid username and password
            else:
                logging.warning("Invalid password for user: %s", username)
                return 'invalid_password'  # Invalid password
        else:
            logging.warning("Invalid username: %s", username)
            return 'invalid_username'  # Invalid username
    except Exception as e:
        logging.error("Error authenticating user: %s", e)
        return 'error'

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Get the form data
    username = request.form['username']
    password = request.form['password']

    # Perform authentication
    auth_result = authenticate(username, password)
    if auth_result is True:
        # If authentication is successful, redirect the user to rough.html
        return redirect('rough.html')
    elif auth_result == 'invalid_password':
        # If authentication fails due to invalid password, render the login form again with an error message
        return render_template('login.html', message='Invalid password.')
    elif auth_result == 'invalid_username':
        # If authentication fails due to invalid username, render the login form again with an error message
        return render_template('login.html', message='Invalid username.')
    else:
        # If authentication fails due to an error, render the login form again with an error message
        return render_template('login.html', message='An error occurred. Please try again later.')

if __name__ == '__main__':
    app.run(debug=True)
