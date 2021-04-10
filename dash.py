from foundation_kit.Arguments import *
import sys

arguments = Arguments('--', sys.argv[1:])
output_to_display = arguments.output_is_window() is False

import logging
from PIL import Image, ImageDraw, ImageFont
from tkinker_renderer import TkinkerRenderer

if output_to_display:
    from lib.waveshare_epd import epd7in5
    epd = epd7in5.EPD()
    screen_width = epd7in5.EPD_WIDTH
    screen_height = epd7in5.EPD_HEIGHT
else:
    screen_width = 640
    screen_height = 384

from GlobalVariables import *
from ui_image_kit.ImageLoader import *
from ui_image_kit.Structures import Context
from dash_scheduler import DashScheduler
from dashes.FullscreenTimeDash import FullscreenTimeDash
from dashes.FullsreenAptMapDash import FullScreenAptMapDash
from dash_kit.DashType import DashType

logging.basicConfig(level=logging.NOTSET)

# Initial setup of the display. Init and full clear cycle.
if output_to_display:
    logging.info("Initializing display.")

    epd.init()
    logging.info("Doing full clear cycle.")
    epd.Clear()

logging.info("Setting up program.")

# Setup the core drawing context
Himage = Image.new('1', (screen_width, screen_height), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)
context = Context(Himage, draw, screen_width, screen_height)

# Global variables

loader = ImageLoader(picdir)

clearAtFinish = True

windowRenderer = None

secondsInAdvance = 10 if output_to_display else 0

#defaultDash = FullscreenTimeDash(context, loader, DashType.FULLSCREEN, secondsInAdvance)
defaultDash = FullScreenAptMapDash(context, loader, DashType.FULLSCREEN, secondsInAdvance)

if output_to_display is False:
    windowRenderer = TkinkerRenderer(screen_width, screen_height)


def render(render_context):
    # Main program
    # try:
    if True:
        logging.info("Running drawing refresh.")
    # except:
    #     logging.critical("Program ran into exception, drawing error message before crash.")
    #     shape = (3, 3, 628, 48)
    #     draw.rectangle(shape, fill=0)
    #     shape = (5, 5, 630, 50)
    #     draw.rectangle(shape, fill=255, outline=255, width=1)
    #     draw.text((10, 10), 'Program ran into exception, sleeping.', font=font24, fill=0)

    # Display fully drawn image, no matter what happened.
    if output_to_display:
        from ui_image_kit import FullscreenMessageWithIcon

        epd.display(epd.getbuffer(Himage))

        if clearAtFinish:
            logging.info("Flag clear at finish set to true, clearing when done.")

            render_context.image = Image.new('1', (epd.width, epd.height), 255)
            render_context.draw = ImageDraw.Draw(Himage)
            message = "powered off"
            icon = loader.get_bw_image('turn-off.png')
            fullscreen_message = FullscreenMessageWithIcon(message, 24, icon, (128, 128), render_context)
            fullscreen_message.draw_view()

            epd.display(epd.getbuffer(Himage))

        # Sleep the display, so it consumes 0 enery
        logging.info("Drawing finished, sleeping display.")
        epd.sleep()
    else:
        # Himage.show('Output')
        windowRenderer.renderImage(render_context.image)


dashScheduler = DashScheduler(
    [defaultDash],
    render_function=render,
    context=context,
    seconds_in_advance=secondsInAdvance
)
dashScheduler.start()

