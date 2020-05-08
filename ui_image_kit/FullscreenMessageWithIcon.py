from GlobalVariables import *
from ui_image_kit.FullscreenView import *
from PIL import Image, ImageDraw, ImageFont
import os


class FullscreenMessageWithIcon(FullscreenView):
    def __init__(self, message, font_size, icon, icon_size, context):
        """Initialize the view with a drawing context and a message with icon to be displayed in the middle of the screen.

        message - String
        icon - PIL Image, black and white
        icon_size - size of the input image, tuple (width, height)
        image - Pillow Image, currently rendered screen to render into
        draw - Pillow ImageDraw
        width - Int screen width
        height - Int screen height
        """
        FullscreenView.__init__(self, context)
        self.message = message
        self.font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), font_size)
        self.icon_size = icon_size
        self.icon = icon.resize(self.icon_size)
        self.spacing = font_size // 2
        self.font_size = font_size

    def draw_view(self):
        """Will clear the screen and draw a message in the middle of it with a 24 sized default Font.
        The icon will be on the left of the message with some space between.
        Must be called every time any property is changed, otherwise changes won't be reflected.

        Overrride in subclasses by calling super().draw_view().
        This way, everything will be drawn with a Painters algorithm, thus layered from bottom to up correctly.
        """

        super().draw_view()

        letter_width = self.font_size // 2
        letter_height = self.font_size

        letter_count = len(self.message)
        message_width = letter_width * letter_count
        message_height = letter_height

        icon_width = self.icon_size[0]
        icon_height = self.icon_size[1]

        icon_x_pos = (self.context.width // 2) - (message_width) - (icon_width // 2 - self.spacing)
        icon_y_pos = (self.context.height // 2) - (icon_height // 2)

        message_x_pos = icon_x_pos + icon_width + self.spacing
        message_y_pos = (self.context.height // 2) - (message_height // 2)

        offset = (icon_x_pos, icon_y_pos)

        self.context.image.paste(self.icon, offset)
        self.context.draw.text((message_x_pos, message_y_pos), self.message, font=self.font, fill=0)

