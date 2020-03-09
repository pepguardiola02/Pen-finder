from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h-1>Hello, World! How are you?</h-1>"

@app.route("/hejhej")
def hej():
    return "Hej på dig lazar!"


app.run()
