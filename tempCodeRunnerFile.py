from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Function to write user data to an Excel file
def write_to_excel(data):
    try:
        # Load existing data from the Excel file
        try:
            df = pd.read_excel('users.xlsx')
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame
            df = pd.DataFrame(columns=['Username', 'Email', 'Password'])

        # Append new data to the DataFrame
        df = df.append({'Username': data[0], 'Email': data[1], 'Password': data[2]}, ignore_index=True)

        # Write the updated DataFrame to the Excel file
        df.to_excel('users.xlsx', index=False)
        print("User added to the Excel file.")
    except Exception as e:
        print(f"Error occurred while writing to Excel file: {e}")


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

    # Write user data to Excel file
    write_to_excel([username, email, password])

    return 'Signup successful!'

if __name__ == '__main__':
    app.run(debug=True)
