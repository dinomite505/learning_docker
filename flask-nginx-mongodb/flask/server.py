"""This module contains a Flask app that connects to a MongoDB server."""

#!/usr/bin/env python
# Importing pymongo Python driver and Flask class
# Third-party imports should come before standard library imports 
from pymongo import MongoClient
from flask import Flask
import os 


app = Flask(__name__)

# Create connection to a MongoDB server, hostname:port
client = MongoClient("mongo:27017")

# Defining a route to Flask app
@app.route('/')
# From root URL execute todo
def todo():
    try:
        # Attempts to execute ismaster to check if MongoDB server's available
        # checks if client is connected to primary or secondary server in replica set.
        client.admin.command('ismaster')
    # Otherwise, app cannot connect to it
    except:
        return "Server is not available"
    return "Hello from MongoDB client!\n" # makes it more readable

# When script is run directly, Flask dev-server starts and listens on host and Flask server port
# Server available on all network interfaces. Enabled Flask dev mode (debug=True)
if __name__== "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER.PORT", 9090), debug=True)
