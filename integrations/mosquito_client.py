import paho.mqtt.client as mqtt
import logging
from integrations import MosquitoEntities as entity


def get_default_entities():
    return [
        entity.BrokerStatus('homeassistant/status'),
        entity.Sensor('homeassistant/sensor/main_sensor_temperature'),
        entity.Sensor('homeassistant/sensor/main_sensor_humidity'),
        entity.Light('homeassistant/light/study_ceiling')
    ]


class MosquitoClient:
    def __init__(self):
        self.mqtt_broker = '192.168.0.2'
        self.client = mqtt.Client("paperdash")
        self.client.username_pw_set() #input here
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.entities = []
        self.connect()

    def connect(self):
        self.client.connect(self.mqtt_broker)
        self.client.loop_start()
        self.subscribe()

    def on_connect(self, client, userdata, flags, rc):
        logging.info("[MQTT] Connected flags ", str(flags), "result code ", str(rc))

    def on_message(self, client, userdata, message):
        logging.info("[MQTT] Received message: ", str(message.payload.decode("utf-8")))

    def subscribe(self):
        entities = get_default_entities()

        for e in entities:
            self.client.subscribe(e.mqtt_topic)
