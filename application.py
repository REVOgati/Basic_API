from flask import Flask

app = Flask(__name__) #Creating instance of the Flask class

@app.route('/') ##defining a route
def index(): # What we want to happen when the route is hit
    return 'Hello!'   
