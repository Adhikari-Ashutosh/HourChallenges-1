# Troublesome Imports here
from flask import Flask,render_template,request
import json
import requests

##########################################################

# App Definition here
app = Flask(__name__)
# Serving through a basic static app.
# Let us retrieve our API keys through our Secrets :shhh:
with open('secrets.json') as user_file:
  file_contents = user_file.read()
secrets = json.loads(file_contents)
API_KEY = secrets['API_KEY']
BASE_URL = "http://api.weatherapi.com/v1/current.json"
LOCATIONS = ['Mumbai','London','San Francisco','Tokyo']
# There is an auto complete method within server. Might just do that but later not right now.

##########################################################
# Creating and doing stuff here!
@app.route("/")
def index():
    # THis is the index page from where we trigger all the queries from.
    return render_template('index.html',loc = LOCATIONS)

# The Weather results
@app.route('/weather')
def print_results():
   location = request.args.get('loc')
   
   r = requests.get(url = BASE_URL+f"?key={API_KEY}&q={location}")
#    return f"{r.json()}"
   return render_template('weather.html',data = r.json())