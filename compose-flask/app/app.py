from flask import Flask

# Flask app instance
app = Flask(__name__)

# Route decorator to associate the 'hello' function with the root URL
# 'hello' function executed when the root URL is accessed
@app.route('/')
def hello():
    return "Hello World. This is Flask app"

# Check if the script is run as the main
if __name__ == '__main__':
    # Start Flask dev server accessible for any network interface. Listening on 8000
    app.run(host='0.0.0.0', port=8000)
