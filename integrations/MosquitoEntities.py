class Sensor:
    def __init__(self, mqtt_topic):
        self.mqtt_topic = mqtt_topic
        self.state = ''
        self.unit_of_measurement = ''
        self.name = ''
        self.friendly_name = ''


class Light:
    def __init__(self, mqtt_topic):
        self.mqtt_topic = mqtt_topic
        self.state_on = False
        self.friendly_name = ''
        self.brightness = 0


class BrokerStatus:
    def __init__(self, mqtt_topic):
        self.mqtt_topic = mqtt_topic
        self.status_online = False
