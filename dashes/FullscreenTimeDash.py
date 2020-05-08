from dash_kit import DashType
from ui_image_kit.FullscreenMessageWithIcon import *
import datetime
from dashes.Dash import Dash


class FullscreenTimeDash(Dash):
    def __init__(self, context, loader, dash_type):
        Dash.__init__(self, dash_type)
        self.context = context
        self.loader = loader
        self.icon = loader.get_bw_image('clock.png')
        self.fullscreen_message = FullscreenMessageWithIcon("", 48, self.icon, (48, 48), self.context)

    def drawContent(self):
        time = datetime.datetime.now().strftime("%H:%M")
        self.fullscreen_message.message = time
        self.fullscreen_message.draw_view()

