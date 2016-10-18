from flask import Flask, render_template, redirect, flash, session
import jinja2

# app is now your new Flask object
app = Flask(__name__)

# You may or may not need, depending on what you're building
app.secret_key = 'something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined


# This route renders the homepage whenever the user visits the root domain.
# Ex. http://yoursite.com/
@app.route('/')
def index():
    """Render homepage and send the user there."""

    return render_template('homepage.html')


# Whevenever you have a form that submits a request (using action="/someaddress"),
# you will need a redirect route and a render route. 

# Redirect route
@app.route('/post-catcher', methods=['POST'])
def post_redirect():
    """ Recieves POST request from form, performs conditional logic and
    operations on the data received in the request. 


    NOTE: This is where any changes or additions to the session must be made.
    Form must look like: <form action='/post-catcher'>...</form>
    """

    return redirect('/post-render')


# Render route
@app.route('/post-render')
def post_render():
    """ Recieves information from post_redirect, and extracts info from session
    and get.args.form().

    NOTE: This is where any information that will be displayed in the Jinja 
    render will be organized and formatted. 
    """


    arg1 = get.args.form('arg1')
    arg2 = get.args.form('arg2')

    return render_template('form-result.html',
                            arg1=arg1,
                            arg2=arg2,
                            arg3="fixed value")





