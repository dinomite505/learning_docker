#!/usr/bin/env python
import os

# Importing flask class and pymongo Python driver
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Create connection to a MongoDB server, hostname:port
client = MongoClient("mongo:27017")

# Defining a route to Flask app
@app.route('/')
# From root URL execute todo
def todo():
    try:
        # Attempts to execute ismaster to check if MongoDB server's available
        # 'ismaster' checks if client is connected to primary server or secondary (slave) server in replica set.
        client.admin.command('ismaster')
    # Otherwise, app cannot connect to it
    except:
        return "Server is not available"
    return "Hello from MongoDB client!\n" # makes it more readable 

# When script is run directly, Flask dev-server starts and listens on host and Flask server port
# Server available on all network interfaces. Enabled Flask dev mode (debug=True)
if __name__== "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER.PORT", 9090), debug=True)