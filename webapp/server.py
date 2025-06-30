"""This code creates the webapp with flask.
"""
from flask import Flask, jsonify

# This creates an instance of the app
app = Flask(__name__)

@app.route("/")
def home():
    """This is the action taken when user reaches webapp LP
    """
    return "Hello, World!"

def json():
    """This returns some JSON data Key:value pair"""
    return {"message": "Hello World"}
