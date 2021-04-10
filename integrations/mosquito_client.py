import paho.mqtt.client as mqtt
import logging
from integrations import MosquitoEntities as entity
import schedule


def get_default_entities():
    return {
        'status': entity.BrokerStatus('homeassistant/status'),
        #'homeassistant/sensor/main_room_temperature': entity.Sensor('homeassistant/sensor/main_room_temperature/#'),
        'homeassistant/light/study_ceiling/state': entity.Light('homeassistant/light/study_ceiling/state'),
    }


class MosquitoClient:
    def __init__(self, entities=get_default_entities()):
        self.mqtt_broker = '-'
        self.client = mqtt.Client("paperdash")
        self.client.username_pw_set('my_username', 'my_password') # input here
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.entities = entities
        self.connect()

    def connect(self):
        self.client.connect(self.mqtt_broker)
        self.subscribe()
        self.client.loop_start()

    def manual_loop(self):
        self.client.loop(timeout=1, max_packets=50)

    def on_connect(self, client, userdata, flags, rc):
        logging.info("[MQTT] Connected flags ", str(flags), "result code ", str(rc))

    def on_message(self, client, userdata, message):
        logging.info("[MQTT] Received message: ", str(message.payload.decode("utf-8")))
        self.update_entity_with_message(message)

    def subscribe(self):
        for e in self.entities.values():
            self.client.subscribe(e.mqtt_topic)

    def update_entity_with_message(self, message):
        updated_entity = self.entities[message.topic]

        if isinstance(updated_entity, entity.Light):
            self.update_light(updated_entity, message.payload.decode())
        if isinstance(updated_entity, entity.Sensor):
            print()

    def update_light(self, light, decoded_payload):
        light.state_on = True if decoded_payload == "on" else False