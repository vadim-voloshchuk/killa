from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://server:super-MEGA_passWORD@localhost/healthy_city'

db.init_app(app)

import routes

app.run(debug=True, host="0.0.0.0")
