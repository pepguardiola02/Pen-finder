from flask import Flask

app = Flask(__name__)

@app.route("/")
def hej():
    return "<title>Pen-finder</title> <header>Pen-Finder</header> "

@app.route("/hejhej")
def hello():
    return "<h1>Hello, World!</h1>"




app.run()
