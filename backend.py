from flask import Flask
app = Flask(__name__)
@app.route("/")
def body():
    print("Hehe")
if __name__ == '__main__':
    app.run(debug=True)
