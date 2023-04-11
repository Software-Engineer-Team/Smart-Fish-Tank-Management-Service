from flask import Flask
from SFTM.routes import home_blueprint
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(home_blueprint)

app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, engineio_logger=True,
                    logger=True, cors_allowed_origins="*", async_mode='eventlet')


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('data')
def handle_light(data):
    print('Received light status:', data)


###############################################################
# import socketio
# import eventlet

# sio = socketio.Server(cors_allowed_origins='*')
# app = socketio.WSGIApp(sio)


# @sio.event
# def connect(sid, environ):
#     print(sid, 'connected')
#     sio.emit('connected_event', {'message': 'Client connected successfully'})


# @sio.on('light')
# def handle_light(sid, data):
#     print('Received light status:', data)
#     # Do something with the light status
#     sio.emit('light_status', {'status': 'ok'})


# @sio.on('temperature')
# def handle_temperature(temp_status):
#     print('Received temperature status:', temp_status)


# @sio.event
# def disconnect(sid):
#     print(sid, 'disconnected')


# if __name__ == '__main__':
#     # Run the app on port 5000
#     eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)

#######################################################
# import engineio
# import eventlet

# eio = engineio.Server(cors_allowed_origins='*')
# app = engineio.WSGIApp(eio)


# @eio.on('connect')
# def connect(sid, environ):
#     print("connect ", sid)


# @eio.on('message')
# def message(sid, data):
#     print("message ", data)
#     eio.send(sid, 'reply')


# @eio.on('disconnect')
# def disconnect(sid):
#     print('disconnect ', sid)


# if __name__ == '__main__':
#     eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)
