import paho.mqtt.client as mqtt


class MosquitoClient:
    def __init__(self):
        self.mqtt_broker = '192.168.0.2'
        self.client = mqtt.Client("paperdash")
        self.client.username_pw_set() #input here
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect

        self.temperature_test = '?'

        self.connect()

    def connect(self):
        self.client.connect(self.mqtt_broker)
        self.client.loop_start()
        self.subscribe('homeassistant/sensor/main_sensor_temperature')

    def on_connect(self, client, userdata, flags, rc):
        print("Connected flags ", str(flags), "result code ", str(rc))

    def on_message(self, client, userdata, message):
        print("received message: ", str(message.payload.decode("utf-8")))

    def subscribe(self, topic):
        self.client.subscribe(topic)
