import sys
import os
import time
import logging
from PIL import Image, ImageDraw, ImageFont
from lib.waveshare_epd import epd7in5

picdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

# Initial setup of the display. Init and full clear cycle.
logging.info("Initializing display.")
epd = epd7in5.EPD()

epd.init()
logging.info("Doing full clear cycle.")
epd.Clear()

logging.info("Setting up program.")
# Global variables
screenWidth = epd7in5.EPD_WIDTH
screenHeight = epd7in5.EPD_HEIGHT

# Resources setup
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

# Basic frame to draw in setup
Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)

# Main program
# try:
if True:
    logging.info("Running drawing refresh.")

    clearAtFinish = False

    letterWidth = 24 / 2
    letterHeight = 24

    message = "I am not an empty frame anymore."

    letterCount = len(message)
    messageWidth = letterWidth * letterCount
    messageHeight = 24

    xPos = (screenWidth / 2) - (messageWidth / 2)
    yPos = (screenHeight / 2) - (messageHeight / 2)

    draw.text((xPos, yPos), message, font=font24, fill=0)

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
epd.display(epd.getbuffer(Himage))

# Sleep the display, so it consumes 0 enery
logging.info("Drawing finished, sleeping display.")
epd.sleep()
