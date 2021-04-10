class Entities:
    def __init__(self):
        self.all = []


class Sensor:
    def __init__(self, mqtt_topic):
        self.mqtt_topic = mqtt_topic
        self.state = 0
        self.unit_of_measurement = '?'


class Light:
    def __init__(self, mqtt_topic):
        self.mqtt_topic = mqtt_topic
        self.state_on = False
        self.brightness = 0


class BrokerStatus:
    def __init__(self, mqtt_topic):
        self.mqtt_topic = mqtt_topic
        self.status_online = False
