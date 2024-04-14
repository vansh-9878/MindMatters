# # from flask import Flask, render_template, request
# # import csv

# # app = Flask(__name__)

# # # Function to write user data to a CSV file
# # def write_to_csv(data):
# #     with open('users.csv', mode='a', newline='') as file:
# #         writer = csv.writer(file)
# #         writer.writerow(data)

# # # Route for the signup form
# # @app.route('/')
# # def signup_form():
# #     return render_template('signup_form.html')

# # # Route to handle form submission
# # @app.route('/signup', methods=['POST'])
# # def signup():
# #     username = request.form['username']
# #     email = request.form['email']
# #     password = request.form['password']

# #     # Write user data to CSV file
# #     write_to_csv([username, email, password])

# #     return 'Signup successful!'

# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask import Flask, render_template, request
# from openpyxl import Workbook

# app = Flask(__name__)

# # Function to write user data to an Excel file
# def write_to_excel(data):
#     wb = Workbook()
#     ws = wb.active
#     ws.append(['Username', 'Email', 'Password'])
#     ws.append(data)
#     wb.save('users.xlsx')

# # Route for the signup form
# @app.route('/')
# def signup_form():
#     return render_template('signup.html')

# # Route to handle form submission
# @app.route('/signup', methods=['POST'])
# def signup():
#     username = request.form['username']
#     email = request.form['email']
#     password = request.form['password']

#     # Write user data to Excel file
#     write_to_excel([username, email, password])

#     return 'Signup successful!'

# if __name__ == '__main__':
#     app.run(debug=True)
