from flask import Flask

app = Flask(__name__)

import config
from app import views

import filters
app.register_blueprint(filters.blueprint)