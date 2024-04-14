# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# import sys
# load_dotenv()
# API_KEY = os.getenv('GEMINI_API_KEY')
# genai.configure(
#     api_key = API_KEY
# )
# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])
# while True:
#     question = input("You:").lower()
#     if question == ["quit","exit","break"]:
#         sys.exit(0)

#     response = chat.send_message(question)
#     print(f"Bot: {response.text}")



from flask import Flask, render_template, jsonify, request
from flask_cors import CORS  # Import CORS extension

import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)

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

# Route for serving the index.html template
@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == "__main__":
    app.run(debug=True)
