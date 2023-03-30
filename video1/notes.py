# flask is a micro web framework for building websites with Python
# usually used as a back end and then another front is connected using a restful api

# flask is a micro framework, instead of a full web framework
# which also means it doesn't include a lot of the Django tools, like authentication



# 1) this is all you have to do to start a website and get it running:
from flask import Flask

app = Flask(__name__)

# if __name__ == '__main__':
#         app.run()
# this if statement ^ needs to be at bottom of file?

# 2) Set up the pages of your website
# def home(): 
#         return "Hello! This is the main page <h1>Hi</h1>"
        # you can write HTML in this string, or some text by itself and it will be displayed 

# 3) We need to tell Flask how to get to the page. To do this, we need to give it a route
@app.route("/", "home")
def home(): 
        return "Hello! This is the main page <h1>Hi</h1>"

# 4) Run the file

# 5) Passing parameters to URL

@app.route("/<name>")
def user(name):
    return f"Hello {name}"



# 6 Redirecting

from flask import redirect, url_for

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
# home is name of function we want to run

if __name__ == '__main__':
        app.run()
# this must be at bottom of file?