
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Route for the login form
@app.route('/')
def login_form():
    return render_template('login.html', message='')  # Passing an empty message initially

# Route to handle login
@app.route('/login_1', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username and password are valid
    if check_credentials(username, password):
        return redirect(url_for('index2'))  # Redirect if credentials are correct
    else:
        return render_template('login.html', message='Invalid username or password.')  # Render login form with error message

# Route for index2.html
@app.route('/index2')
def index2():
    return render_template('index2.html')

# Function to check user credentials
def check_credentials(username, password):
    # You need to implement the logic to check the credentials against your Excel file here
    df = pd.read_excel("C:\\Users\\91981\\vscode\\UltraMatrix\\users.xlsx")
    match = df[(df['Username'] == username) & (df['Password'] == password)]

    # If a match is found, return True; otherwise, return False
    if not match.empty:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)
