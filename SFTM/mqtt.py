from SFTM import mqtt_client
TOPICS = ["/feeds/yolo-temp"]
mqtt_client.subscribe(TOPICS)


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    print(rc)
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe(TOPIC)  # subscribe topic
    else:
        print('Bad connection. Code:', rc)


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(
        'Received message on topic: {topic} with payload: {payload}'.format(**data))
