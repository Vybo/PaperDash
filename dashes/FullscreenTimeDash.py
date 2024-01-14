import datetime

from dashes.Dash import Dash
from ui_image_kit.FullscreenMessageWithIcon import *


class FullscreenTimeDash(Dash):
    def __init__(self, context, loader, dash_type, seconds_in_advance):
        Dash.__init__(self, dash_type, seconds_in_advance)
        self.context = context
        self.loader = loader
        self.icon = loader.get_bw_image('clock.png')
        self.fullscreen_message = FullscreenMessageWithIcon("", 48, self.icon, (48, 48), self.context)

    def draw_content(self):
        self.context.draw.rectangle((0, 0, self.context.width, self.context.height), fill=255)
        time = datetime.datetime.now()
        adjusted_time = time - datetime.timedelta(seconds=self.seconds_in_advance)
        formatted_time = adjusted_time.strftime("%H:%M")
        self.fullscreen_message.message = formatted_time
        self.fullscreen_message.draw_view()
