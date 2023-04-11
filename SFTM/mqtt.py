# import sys
# from Adafruit_IO import MQTTClient

# ADAFRUIT_IO_KEY = 'aio_PHNU25ma1EQiIVlSYlVzJkXrp6Lt'
# ADAFRUIT_IO_USERNAME = 'tamquattnb123'
# FEED_IDS = ['yolo-temp', 'yolo-light', 'yolo-fan']


# def connected(client):
#     print('Connected to Adafruit IO!  Listening for {0} changes...'.format(
#         ', '.join(FEED_IDS)))
#     for feed_id in FEED_IDS:
#         client.subscribe(feed_id)


# def subscribe(client, userdata, mid, granted_qos):
#     print('Subscribed to {0} with QoS {1}'.format(
#         FEED_IDS[mid-1], granted_qos[0]))


# def disconnected(client):
#     print('Disconnected from Adafruit IO!')
#     sys.exit(1)


# def message(client, feed_id, payload):
#     print('Feed {0} received new value: {1}'.format(feed_id, payload))


# client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# client.on_connect = connected
# client.on_disconnect = disconnected
# client.on_message = message
# client.on_subscribe = subscribe

# client.connect()

# client.loop_background()
