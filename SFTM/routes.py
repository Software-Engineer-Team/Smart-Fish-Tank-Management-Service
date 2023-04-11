from flask import Blueprint

home_blueprint = Blueprint('home_blueprint', __name__)


@home_blueprint.route('/')
def home_page():
    return "Server is running on port 5000!!!"
