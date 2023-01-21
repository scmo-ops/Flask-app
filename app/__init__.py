from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_obejct(Config) # This line is telling flask to read and apply my config file.

from app import routes
