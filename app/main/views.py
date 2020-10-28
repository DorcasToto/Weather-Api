from ..requests import getWeather
from flask import render_template
from flask import jsonify
import urllib.request,json
from . import main

@main.route("/weather/api/v1.0/current", methods=['GET'])
def index():
    response =  getWeather('Kericho')
    # import pdb; pdb.set_trace()
    return render_template("index.html",response = response)