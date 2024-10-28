from flask import Flask

app = Flask(__name__) #Creating instance of the Flask class

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app) #DB IS AN INSTANCE OF sqlalchemy and then pass our app

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/') ##defining a route
def index(): # What we want to happen when the route is hit
    return 'Hello!'   

#Create an app to get drinks(get request)
@app.route('/drinks')
def get_drinks():
    return {'drinks': 'Grayson'}

#Connecting to a database
#We will define all things we want to store in our database as modules (line 4)
