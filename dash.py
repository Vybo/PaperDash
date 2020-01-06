from foundation_kit.Arguments import *
import sys

arguments = Arguments('--', sys.argv[1:])
output_to_display = arguments.output_is_window() is False

import os
import time
import datetime
import logging
from PIL import Image, ImageDraw, ImageFont

if output_to_display:
    from lib.waveshare_epd import epd7in5
    epd = epd7in5.EPD()
    screen_width = epd7in5.EPD_WIDTH
    screen_height = epd7in5.EPD_HEIGHT
else:
    screen_width = 640
    screen_height = 384

from GlobalVariables import *
from ui_image_kit.FullscreenMessageWithIcon import *
from ui_image_kit.ImageLoader import *
from ui_image_kit.Structures import Context

logging.basicConfig(level=logging.NOTSET)

# Initial setup of the display. Init and full clear cycle.
if output_to_display:
    logging.info("Initializing display.")

    epd.init()
    logging.info("Doing full clear cycle.")
    epd.Clear()

logging.info("Setting up program.")
# Global variables



# Setup the core drawing context
Himage = Image.new('1', (screen_width, screen_height), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)
context = Context(Himage, draw, screen_width, screen_height)

loader = ImageLoader(picdir)

clearAtFinish = True

# Main program
# try:
if True:
    logging.info("Running drawing refresh.")

    time = datetime.datetime.now().strftime("%H:%M")
    message = time
    icon = loader.get_bw_image('clock.png')
    fullscreenMessage = FullscreenMessageWithIcon(message, 48, icon, (48, 48), context)
    fullscreenMessage.draw_view()

# except:
#     logging.critical("Program ran into exception, drawing error message before crash.")
#     shape = (3, 3, 628, 48)
#     draw.rectangle(shape, fill=0)
#     shape = (5, 5, 630, 50)
#     draw.rectangle(shape, fill=255, outline=255, width=1)
#     draw.text((10, 10), 'Program ran into exception, sleeping.', font=font24, fill=0)

# Display fully drawn image, no matter what happened.
if output_to_display:
    epd.display(epd.getbuffer(Himage))

    if clearAtFinish:
        logging.info("Flag clear at finish set to true, clearing when done.")

        Himage = Image.new('1', (epd.width, epd.height), 255)
        draw = ImageDraw.Draw(Himage)
        context = Context(Himage, draw, screen_width, screen_height)
        message = "powered off"
        icon = loader.get_bw_image('turn-off.png')
        fullscreenMessage = FullscreenMessageWithIcon(message, 24, icon, (128, 128), context)
        fullscreenMessage.draw_view()

        epd.display(epd.getbuffer(Himage))

    # Sleep the display, so it consumes 0 enery
    logging.info("Drawing finished, sleeping display.")
    epd.sleep()
else:
    Himage.show('Output')

