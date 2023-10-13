from __main__ import app
from flask import request
from fictitious_nn import fictitous_function
import json


@app.route("/")
def hello():
    return "It's working!" 

@app.route("/processing", methods=['POST'])
def processing():
    coords_lst = request.json['coords']
    return json.dumps(fictitous_function(coords_lst))
