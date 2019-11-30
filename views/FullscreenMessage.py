from GlobalVariables import *
from views.FullscreenView import *
from PIL import Image, ImageDraw, ImageFont
import os


class FullscreenMessage(FullscreenView):
    def __init__(self, message, draw, width, height):
        """Initialize the view with a drawing context and a message to be displayed in the middle of the screen.
        context - Pillow ImageDraw
        message - String
        """
        FullscreenView.__init__(self, draw, width, height)
        self.message = message
        self.font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    def draw_view(self):
        """Will clear the screen and draw a message in the middle of it with a 24 sized default Font.
        Must be called every time any property is changed, otherwise changes won't be reflected.

        Overrride in subclasses by calling super().draw_view().
        This way, everything will be drawn with a Painters algorithm, thus layered from bottom to up correctly.
        """

        super().draw_view()

        letter_width = 24 / 2
        letter_height = 24

        letter_count = len(self.message)
        message_width = letter_width * letter_count
        message_height = letter_height

        xPos = (self.width / 2) - (message_width / 2)
        yPos = (self.height / 2) - (message_height / 2)

        self.draw.text((xPos, yPos), self.message, font=self.font, fill=0)
