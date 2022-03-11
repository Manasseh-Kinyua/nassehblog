from flask import Flask
from flask_bootstrap import Bootstrap

#initializing the app
app = Flask(__name__)

#initializing flask extensions
bootstrap = Bootstrap()

from app import views
