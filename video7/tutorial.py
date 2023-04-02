from flask import Flask, request, redirect, url_for, render_template, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.sqlite3'
# users is the name of the table we will be referencing^^
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(days = 5)

db = SQLAlchemy(app)

# we will make a class below to define a model/object/table in our database
# we write the models in Python
# the class users will be using the db.Model as the inheritance, so it can inherit methods and things

class users(db.Model):
    _id = db.Column("id", db.integer, primary_key=True)
    # every object in the database needs to have a unique identifier
    # it could be a string or boolean (boolean if there are only 2 values, 1 True and 1 False)
    # primary_key = true means this is how we can reference all these objects
      # when you create a user, you don't have to POST an id for them, they will create one automatically because it's a primary key
    name = db.Column(db.String(100))
    # if you don't put the first parameter in, it will go with whatever you name the variable (here it will be "name")
    # 100 is maximum number of characters for the name string
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user", methods=['POST', 'GET'])
def user():
    email = None
    # if we end up passing in a None email, then the placeholder value will be in the email box (the placeholder="Enter email" in the HTML)

    if "user" in session:
        user = session["user"]

        if request.method == 'POST':
            # if we got to this page through POST
            email = request.form["email"]
            session["email"] = email
            flash("email was saved!")
        else:
            # if it was a GET
            if "email" in session:
             email = session["email"]
            

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
        flash("You have been logged out!", "info")
        session.pop("user", None)
        session.pop("email", None)
        return redirect(url_for("login"))
    

if __name__ == '__main__':
    db.create_all()
    # make sure this is above app.run so the db exists
    app.run(debug=True)

