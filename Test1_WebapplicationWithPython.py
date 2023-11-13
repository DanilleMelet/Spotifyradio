# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 18:39:15 2023

@author: Danille
"""
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and the associated function to handle the request
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application if this script is the main program
if __name__ == '__main__':
    app.run()
