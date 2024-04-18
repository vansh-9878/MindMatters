import logging
from flask import Flask, render_template, request, redirect, session, jsonify, send_from_directory
import pandas as pd
import os
from dotenv import load_dotenv
from flask_cors import CORS  # Import CORS extension
import google.generativeai as genai
import random
import string


app = Flask(__name__)

# Configure session secret key
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Enable CORS for all routes
CORS(app)

# Load API key from environment variables
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

# Configure Generative AI with the API key
genai.configure(api_key=API_KEY)

# Create GenerativeModel and start chat
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

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
            # Store username in session
            session['username'] = username
            # If authentication is successful, redirect the user to prof.html
            return redirect('prof.html')
        else:
            # If authentication fails, render the login form again with an error message
            return render_template('login.html', message='Invalid username or password.')
    else:
        # If it's a GET request, render the login form
        return render_template('login.html')

# Route for the prof.html page
@app.route('/prof.html')
def profile():
    # Check if username is stored in session
    if 'username' in session:
        # If username is in session, render the profile page with the username
        return render_template('prof.html', username=session['username'])
    else:
        # If username is not in session, redirect to login page
        return redirect('/login')

# Route for serving the index.html template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index_html():
    return render_template('index.html')

@app.route('/games.html')
def games_html():
    return render_template('games.html')

@app.route('/form.html')
def form_html():
    return render_template('form.html')

@app.route('/therepist.html')
def therepist_html():
    return render_template('therepist.html')

@app.route('/script.js')
def script():
    return render_template('script.js')

@app.route('/style.css')
def style_css():
    return render_template('style.css')

app.route('/nav.css')
def nav_css():
    return render_template('nav.css')

app.route('/games.css')
def games_css():
    return render_template('games.css')

app.route('/form.css')
def form_css():
    return render_template('form.css')

# Route to handle user input and return bot response
@app.route('/get_resp', methods=['POST'])
def get_response():
    # Retrieve user's message from the request
    user_input = request.json['message']
    
    # Log the user's message
    print("User's Message:", user_input)

    # Send the user's message to the Generative AI chatbot
    response = chat.send_message(user_input)

    # Log the bot's response
    print("Bot's Response:", response.text)

    # Return the bot's response as JSON
    return jsonify({'response': response.text})

# Route for the signup form
@app.route('/sign', methods=['GET', 'POST'])
def signup_form():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Write user data to the Excel file
        write_to_excel({'Username': username, 'Email': email, 'Password': password})

        # Redirect to login page after successful signup
        return redirect('/login')
    else:
        return render_template('signup.html')

# Route for the login page
@app.route('/login')
def login_form():
    return render_template('login.html')

@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.ico')

@app.route('/index2.html')
def index2():
    return render_template('index2.html')



def generate_meeting_code():
    # Generate three segments of alphabets or digits
    segment1 = ''.join(random.choices(string.ascii_lowercase, k=3))
    segment2 = ''.join(random.choices(string.ascii_lowercase, k=4))
    segment3 = ''.join(random.choices(string.ascii_lowercase, k=3))

    # Concatenate the segments with dashes
    return f"{segment1}-{segment2}-{segment3}"


@app.route('/generate-meet-link', methods=['POST'])
def generate_meet_link():
    data = request.json
    selected_slot = data.get('slot')
    selected_date = data.get('date')

    meeting_code = generate_meeting_code()

    # You can replace this logic with your own to generate the Google Meet link
    google_meet_link = f"https://meet.google.com/new?date={selected_date}&time={selected_slot}&code={meeting_code}"

    return jsonify({'meeting_link': google_meet_link, 'meeting_code': meeting_code})


# USER SECTION

def write_to_excel1(data):
    try:
        # Read existing data from Excel file
        try:
            df = pd.read_excel('therapists.xlsx')
        except FileNotFoundError:
            # If file doesn't exist, create a new DataFrame
            df = pd.DataFrame(columns=['Username', 'Email', 'Password'])

        # Append new user data to DataFrame
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

        # Write DataFrame back to Excel file
        df.to_excel('therapists.xlsx', index=False)
        logging.debug("Data written to Excel file successfully.")
    except Exception as e:
        logging.error("Error writing to Excel database:", e)

# Function to check if the username and password are valid
def authenticate1(username, password):
    try:
        df = pd.read_excel('therapists.xlsx')
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

@app.route('/therapist_login', methods=['GET', 'POST'])
def therapist_login():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']

        # Perform authentication
        if authenticate1(username, password):
            # Store username in session
            session['username'] = username
            # If authentication is successful, redirect the user to prof.html
            return redirect('prof.html')
        else:
            # If authentication fails, render the login form again with an error message
            return render_template('therapist_login.html', message='Invalid username or password.')
    else:
        # If it's a GET request, render the login form
        return render_template('therapist_login.html')
    # return render_template('therapist_login.html')

@app.route('/therapist_signup', methods=['GET', 'POST'])
def therapist_signup():
    # return render_template('therapist_signup.html')
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Write user data to the Excel file
        write_to_excel1({'Username': username, 'Email': email, 'Password': password})

        # Redirect to login page after successful signup
        return redirect('/therapist_login')
    else:
        return render_template('therapist_signup.html')

@app.route('/therapist_login')
def therapist_login_form():
    return render_template('therapist_login.html')

@app.route('/therapist_signup')
def therapist_signup_form():
    return render_template('therapist_signup.html')

@app.route('/tpl')
def tpl():
    return render_template('tpl.html')

@app.route('/tps')
def tps():
    return render_template('tps.html')

if __name__ == '__main__':
    app.run(debug=True)
