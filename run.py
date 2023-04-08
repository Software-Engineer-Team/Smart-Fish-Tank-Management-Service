import os
from SFTM import app, socketio

if __name__ == '__main__':
    socketio.run(app, port=int(os.environ.get('PORT', 5000)))

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
