# video 5 is about sessions
# how we can do the previous video's code better

# a session is something you use while user is on website, then when you leave it disappears
# ex: a user logs in, a new session is created
# as they go through pages, they have the session data
# with the user's info and other info
# as soon as the user leaves, all the session data is gone
# when they login back in, the session data reloads
# sessions are temporary, stored on the server, not the client side
# they are designed as a quick way to access information and to pass things around our server

# import session from flask

#   session["user"] = user
# all the session data we store is encrypted on the server
# that means we need to define a secret key, which is how you encrypt and decrypt the data


    # if "user" in session:
    #     user = session["user"]
# print session to see it in the terminal
# if you close your browser, the session data will be deleted from the server
# so if you want to get back to the user page, 
# you'll have to log in again, which then create a new session

    # session.pop("user", None)
    # Tim does not know why None is there, but it just needs to be there


# from datetime import timedelta
# app.permanent_session_lifetime = timedelta(days = 5)
# ...
# def login():
#     if request.method == 'POST':
#         session.permanent = True
# now we are storing permenant session data for 5 days
# you can also do minutes = 5, etc.
# then go down and set session.permanent = True, so it will then last for that long, even when you close browser/window
# by default, this is set to false

