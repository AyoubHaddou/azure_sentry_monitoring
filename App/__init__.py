from flask import Flask
import os 

app = Flask(__name__)

from .routes import *

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY