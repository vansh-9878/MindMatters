from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route for the profile page
@app.route('/profile/<username>')
def profile(username):
    # Pass the username to the profile template
    return render_template('profile.html', username=username)

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('profile', username='username')) # Redirect to profile page

if __name__ == '__main__':
    app.run(debug=True)
