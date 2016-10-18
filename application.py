from flask import Flask, render_template, redirect, flash, session
import jinja2

app = Flask(__name__)

app.secret_key = 'something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined



@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")