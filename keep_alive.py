##
# Keep bot working

from flask import Flask       # flask server
from threading import Thread  # thread handlers

# Start a flask server
app = Flask('') 

# setting main route
@app.route('/')
def home():
    return "I am alive yet"

# ask flask server to run
def run():
    app.run(host='0.0.0.0', port=8080)

# run server
def keep_alive(): 
    t = Thread(target=run)
    t.start()