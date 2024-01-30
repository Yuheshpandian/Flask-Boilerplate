from flask import Flask, render_template, redirect, url_for, abort
from logging import FileHandler, WARNING

app = Flask(__name__)

# All routes are defined below
# Modify or Add routes according to your site idea

@app.route("/")
def default():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

# definition of routes ends here

# Error handlers are defined here
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404page.html")

@app.errorhandler(500)
def server_error(e):
    return render_template("500page.html")

@app.errorhandler(403)
def forbidden(e):
    return render_template("403page.html")
#  definition of error handlers ends here

# your website's configuration is initialized in this line
app.config.from_pyfile("config.py")

#This code snippet works only when the debug mode is False that is only on production. This code adds the internal server error of your site when it is on production to the "errorlog.txt" file.
if not app.debug:
    file_handler = FileHandler("errorlog.txt")
    file_handler.setLevel(WARNING)
    app.logger.addHandler(file_handler)

# Runs only when the file run directly without importing it
if __name__ == "__main__":
    app.run()