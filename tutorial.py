from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    # you can write HTML in this string, or some text by itself and it will be displayed 
    return "Hello! this is the main page <h1>HELLO</h1>"


if __name__ == '__main__':
    app.run()

# this is all you have to do to start a website and get it running