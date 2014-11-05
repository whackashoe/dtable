from flask import Flask
import filters

app = Flask(__name__)
app.register_blueprint(filters.blueprint)
from app import views
