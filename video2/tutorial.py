from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', content = "this is the content prop", listOfStuff = ['pizza', 'hello', 'ice cream'])

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run()
