from flask import Flask
# from SFTM.mqtt import *
from SFTM.routes import home_blueprint
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(home_blueprint)

app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, engineio_logger=True,
                    logger=True, cors_allowed_origins="*", cors_credentials=True)


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('light')
def handle_light(light_status):
    print('Received light status:', light_status)


@socketio.on('temperature')
def handle_temperature(temp_status):
    print('Received temperature status:', temp_status)
