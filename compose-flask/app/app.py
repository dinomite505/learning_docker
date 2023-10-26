from flask import Flask

# Flask app instance
app = Flask(__name__)

# Route decorator to associate the 'hello' function with the root URL
# 'hello' function executed when the root URL is accessed
@app.route('/')
def hello():
    return "Hello World. This is Flask app"
