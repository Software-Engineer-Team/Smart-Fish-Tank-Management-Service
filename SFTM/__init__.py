from flask import Flask
from SFTM.routes import home_blueprint
from SFTM.mqtt import *
app = Flask(__name__)
app.register_blueprint(home_blueprint)

mqtt_client = Mqtt(app)
