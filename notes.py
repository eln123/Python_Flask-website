# flask is a micro web framework for building websites with Python
# usually used as a back end and then another front is connected using a restful api

# flask is a micro framework, instead of a full web framework
# which also means it doesn't include a lot of the Django tools, like authentication


# Steps:
# 1) this is all you have to do to start a website and get it running:
    # from flask import Flask
    # app = Flask(__name__)
    # if __name__ == '__main__':
        #     app.run()

# 2) Set up the pages of your website
        # ex: def home(): is your home page
                # return "Hello! This is the main page <h1>Hi</h1>"
            # you can write HTML in this string, or some text by itself and it will be displayed 

# 3) We need to tell Flask how to get to the page. To do this, we need to give it a route
        # ex: @app.route("/")

# 4) Run the file