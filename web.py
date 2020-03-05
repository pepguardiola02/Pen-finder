from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hejhej")
def Hej():
    return "Hej på dig lazar!"


app.run()
