from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"

@app.route("/hejhej")
def hej():
    return "Hej på dig lazar!"


app.run()
