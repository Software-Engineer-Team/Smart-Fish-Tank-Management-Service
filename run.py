import os
from SFTM import app, socketio

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=int(
        os.environ.get('PORT', 5000)), use_reloader=True, debug=True)
