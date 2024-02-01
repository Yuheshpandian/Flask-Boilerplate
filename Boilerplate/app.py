# Importing Required Packages
from flask import Flask, render_template, redirect, url_for, abort
from logging import FileHandler, WARNING

# Creating a app instance
app = Flask(__name__)

# website's configuration is initialized in this line in relative to config.py file
app.config.from_pyfile("config.py")


# All routes are defined below
# Modify or Add routes according to your site idea

# Redirects to the home page
@app.route("/")
def default():
    return redirect(url_for("home"))

# Home Page
@app.route("/home")
def home():
    return render_template("home.html")

# Definition of routes ends here

# Error handlers are defined here

# 404 Error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404page.html")

# 500 Error
@app.errorhandler(500)
def server_error(e):
    return render_template("500page.html")

# 403 Error
@app.errorhandler(403)
def forbidden(e):
    return render_template("403page.html")
    
# Definition of error handlers ends here


#This code snippet works only when the debug mode is False that is only on production. This code adds the internal server error of your site when it is on production to the "errorlog.txt" file.
if not app.debug:
    file_handler = FileHandler("errorlog.txt")
    file_handler.setLevel(WARNING)
    app.logger.addHandler(file_handler)

# Runs only when the file is run directly by not importing
if __name__ == "__main__":
    app.run()
