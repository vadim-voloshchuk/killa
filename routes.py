from __main__ import app, db
from flask import request
from model import Files
from fictitious_nn import fictitous_function
import json


@app.route("/")
def hello():
    return "It's working!" 

@app.route("/processing", methods=['POST'])
def processing():
    coords_lst = request.json['coords']
    return json.dumps(fictitous_function(coords_lst))

@app.route("/upload file", methods=['POST'])
def upload_file():
    file = request.files['file']
    new_file = Files(file=file.stream.read())
    db.session.add(new_file)
    db.session.commit()

    return 'OK'
