import sys
import os
import time
import logging
from PIL import Image, ImageDraw, ImageFont
from lib.waveshare_epd import epd7in5

from GlobalVariables import *
from ui_image_kit.FullscreenMessage import *
from foundation_kit.Arguments import *

logging.basicConfig(level=logging.NOTSET)

arguments = Arguments('--', sys.argv[1:])
output_to_display = arguments.output_is_window() is False

epd = epd7in5.EPD()

# Initial setup of the display. Init and full clear cycle.
if output_to_display:
    logging.info("Initializing display.")

    epd.init()
    logging.info("Doing full clear cycle.")
    epd.Clear()

logging.info("Setting up program.")
# Global variables

screen_width = epd7in5.EPD_WIDTH
screen_height = epd7in5.EPD_HEIGHT

# Setup the core drawing context
Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)

# Main program
# try:
if True:
    logging.info("Running drawing refresh.")

    clearAtFinish = False

    message = "I am not an empty frame anymore."

    fullscreenMessage = FullscreenMessage(message, draw, screen_width, screen_height)
    fullscreenMessage.draw_view()

    if clearAtFinish:
        logging.info("Flag clear at finish set to true, clearing when done.")
        epd.Clear()
        Himage = Image.open(os.path.join(picdir, '7in5.bmp'))

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
    # Sleep the display, so it consumes 0 enery
    logging.info("Drawing finished, sleeping display.")
    epd.sleep()
else:
    Himage.show('Output')

