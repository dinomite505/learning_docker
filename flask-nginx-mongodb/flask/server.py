#!/usr/bin/env python
import os

# Importing flask class and pymongo Python driver
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Create connection to a MongoDB server, hostname:port
client = MongoClient("mongo:207017")


