
# DEPLOYMENT NOTES

# To make publically accessible
# flask run --host=0.0.0.0


from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page hadsf '

@app.route('/hello')
def hello():
    return 'Hello, World'