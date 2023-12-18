from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello! this is laba#9, by Sitalova Anastasia BIT-231'

if name == "__main__":
        app.run(host="0.0.0.0")
