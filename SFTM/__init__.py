from flask import Flask
from SFTM.routes import home_blueprint

app = Flask(__name__)
app.register_blueprint(home_blueprint)
