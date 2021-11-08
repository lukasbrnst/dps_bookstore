# -*- encoding: utf-8 -*-

from flask import Flask
import os
from web_app.flaskdb import db

import sys
sys.path.append(__file__+"/..") 
from backend.db_tables import Books



# Inject Flask magic
app = Flask(__name__)

# App Config - the minimal footprint
app.config['TESTING'   ] = True 
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI_DPSBOOK']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db.init_app(app)
with app.app_context():
    db.create_all()
    

# Import routing to render the pages
from . import views
