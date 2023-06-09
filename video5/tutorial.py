from flask import Flask, request, redirect, url_for, render_template, session
from datetime import timedelta
# we are using this, to set up the maximum amount of time our session can last for

app = Flask(__name__)
app.secret_key = "hello"
# all the session data we store is encrypted on the server
# that means we need to define a secret key, which is how you encrypt and decrypt the data

app.permanent_session_lifetime = timedelta(days = 5)
# now we are storing permenant session data for 5 days
# you can also do minutes = 5, etc.
# then go down and set session.permanent = True, so it will then last for that long, even when you close browser/window
# by default, this is set to false


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user", user=user))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    # Tim does not know why None is there, but it just needs to be there
    return redirect(url_for("login"))
    # so when we go to "/logout", it deletes the session and redirects us to the "/login" page
    


if __name__ == '__main__':
    app.run(debug=True)

