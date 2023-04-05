from flask import Flask
from SFTM.routes import home_blueprint
from flask_mqtt import Mqtt
print(__name__)
app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'wss://io.adafruit.com:433/mqtt'
app.config['MQTT_USERNAME'] = 'tamquattnb123'
app.config['MQTT_PASSWORD'] = 'aio_SHSq53Ktw0oOxm77yXrUWZRm9Rt9'
app.config['MQTT_TLS_ENABLED'] = True
app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
# If your broker supports TLS, set it True
app.register_blueprint(home_blueprint)

mqtt_client = Mqtt(app)
