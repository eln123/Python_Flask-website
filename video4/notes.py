# in video 4, we talk about GET and POST http methods
# how they send info to client/server, what they are, etc.
# uses authentication example


# GET is the most common way to get/send/exchange information to/from a website
# ** but it is insecure method
# POST is a safer alternative
# GET is typically used for a link to redirect or parameter passed in through URL
# it is insecure and you send what you don't care about being secure
# POST is secure and usually for form data and something you won't save on web server itself, unless you are going to send it to a database


# login.html
# for the <form> tag, action="#" means it will redirect to the url "/#" once the form is submitted
# the # sound means go back to the same page you were on

# request.form in tutorial.py
# the request object is a dictionary
# make sure the request.method == "POST", not "GET"