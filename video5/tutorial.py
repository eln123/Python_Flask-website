from flask import Flask, request, redirect, url_for, render_template, session

app = Flask(__name__)
app.secret_key = "hello"
# all the session data we store is encrypted on the server
# that means we need to define a secret key, which is how you encrypt and decrypt the data

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form["nm"]
        session["user"] = user
        # the session stores data as a dictionary
        #["user"] user is a key, user is the vlaue
        return redirect(url_for("user", user=user))
    else:
        return render_template("login.html")

@app.route("/<user>")
def user(user):
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)

