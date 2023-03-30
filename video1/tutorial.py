from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # you can write HTML in this string, or some text by itself and it will be displayed 
    return "Hello! this is the main page <h1>HELLO</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
# home is name of function we want to run

if __name__ == '__main__':
    app.run()

# this is all you have to do to start a website and get it running