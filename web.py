from flask import Flask , request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hej():
    if request.methods == 'POST':
        return
    else: 
        return

    return "<title>Pen-finder</title> <header>Pen-Finder</header>"   



@app.route("/hejhej")
def hello():
    return "<h1>Hello, World!</h1>"




app.run()
