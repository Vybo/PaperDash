from GlobalVariables import *
from ui_image_kit.FullscreenView import *
import os
from PIL import Image, ImageDraw, ImageFont
import datetime
from dashes.Dash import Dash
from integrations import mosquito_client


class FullScreenAptMapDash(Dash):
    def __init__(self, context, loader, dash_type, seconds_in_advance):
        Dash.__init__(self, dash_type, seconds_in_advance)
        self.context = context
        self.loader = loader
        self.apt_map = loader.get_bw_image('apt.png')
        # There would be an image resize, but this image is exact fit for the display
        self.font_big = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 48)
        self.font_small = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        self.font_tiny = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 14)
        self.bulb_off_icon = loader.get_bw_image('lightbulb-outline.png')
        self.bulb_on_icon = loader.get_bw_image('lightbulb-on.png')

        # self.mqtt = mosquito_client.MosquitoClient()


    def drawContent(self):
        # Fill white over everything
        self.context.draw.rectangle((0, 0, self.context.width, self.context.height), fill=255)
        time = datetime.datetime.now()
        adjusted_time = time - datetime.timedelta(seconds=self.seconds_in_advance)
        formatted_time = adjusted_time.strftime("%H:%M")
        formatted_date = adjusted_time.strftime("%d.%m.%Y")

        # Map
        self.draw_map()

        # Date & Time
        clock_offset = (490, 230)
        date_offset = (clock_offset[0] + 6, clock_offset[1] + self.font_big.size)
        clock_box = (clock_offset[0], clock_offset[1], 620, date_offset[1] + 32)  # ugly ugly ugly

        self.context.draw.rectangle(clock_box, fill=255, outline=0, width=2)
        self.context.draw.text(clock_offset, formatted_time, font=self.font_big, fill=0)
        self.context.draw.text(date_offset, formatted_date, font=self.font_small, fill=0)

        # Broker status
        broker_msg_offset = (78, 120)
        broker_msg_box = (broker_msg_offset[0], broker_msg_offset[1], broker_msg_offset[0]*2, sum(list(broker_msg_offset)))
        self.context.draw.rectangle(broker_msg_box, fill=255)
        self.context.draw.text(broker_msg_offset, 'broker\noffline', font=self.font_small, fill=0)

        # Bathroom values
        bathroom_msg_offset = (114, 48)
        self.draw_atm_sensor_box(bathroom_msg_offset, 20.5, 80)

        # Bedroom values
        bedroom_msg_offset = (380, 130)
        self.draw_atm_sensor_box(bedroom_msg_offset, 21.5, 32.9)
        bedroom_bulb1_offset = (410, 80)
        self.draw_bulb(bedroom_bulb1_offset, False)
        bedroom_bulb2_offset = (460, 140)
        self.draw_bulb(bedroom_bulb2_offset, True)

        # Hall values
        hall_msg_offset = (194, 120)
        self.draw_atm_sensor_box(hall_msg_offset, 23, 40)
        hall_bulb_offset = (263, 140)
        self.draw_bulb(hall_bulb_offset, True)

        # Dining room values
        dining_room_bulb_offset = (246, 210)
        self.draw_bulb(dining_room_bulb_offset, True)

        # Kitchen values
        kitchen_bulb_offset = (153, 269)
        self.draw_bulb(kitchen_bulb_offset, True)

        # Living room values
        living_room_msg_offset = (294, 150)
        self.draw_atm_sensor_box(living_room_msg_offset, 24.5, 45)
        living_room_bulb_offset = (375, 252)
        self.draw_bulb(living_room_bulb_offset, True)

        # Study values
        study_bulb_offset = (263, 50)
        self.draw_bulb(study_bulb_offset, True)

    def draw_map(self):
        apt_map_offset = (0, 0)
        self.context.image.paste(self.apt_map, apt_map_offset)

    def draw_atm_sensor_box(self, offset, temperature_value, humidity_value):
        box = (offset[0] - 4, offset[1] - 4, offset[0] + 66, offset[1] + 36)
        formatted_temp = "{:.1f}".format(temperature_value)
        formatted_hum = "{:}".format(round(humidity_value,1))
        self.context.draw.rectangle(box, fill=255)
        self.context.draw.text(offset, f'T: {formatted_temp} °C\nH: {formatted_hum} %', font=self.font_tiny, fill=0)

    def draw_bulb(self, offset, status_is_on):
        icon = self.bulb_on_icon if status_is_on else self.bulb_off_icon
        self.context.image.paste(icon, offset)



