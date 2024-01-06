from foundation_kit.Arguments import *
import sys

arguments = Arguments('--', sys.argv[1:])
output_to_display = arguments.output_is_window() is False

import logging
from PIL import Image, ImageDraw, ImageFont

if output_to_display == False:
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
from dashes.PhotoDash import PhotoDash
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

loader = ImageLoader(photodir)

clearAtFinish = False

windowRenderer = None

secondsInAdvance = 10 if output_to_display else 0

clearInterval = 5
refreshCounter = 0

defaultDash = PhotoDash(context, loader, DashType.FULLSCREEN, secondsInAdvance)

if output_to_display is False:
    windowRenderer = TkinkerRenderer(screen_width, screen_height)


def render(render_context, current_refresh, clear_interval):
    # Main program

    logging.info("Running render function.")

    # Rendering to real display. Display fully drawn image, no matter what happened.
    if output_to_display:
        epd.init()

        if current_refresh == clear_interval:
            logging.info("Hit refresh threshold, doing full clean..")
            epd.Clear()

        logging.info("Drawing new content.")
        epd.display(epd.getbuffer(Himage))

        # Clear at finish flag displays message on the display and exits the application
        if clearAtFinish:
            from ui_image_kit import FullscreenMessageWithIcon
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
    # Rendering to Window for debugging. Use "--output window" argument.
    else:
        windowRenderer.renderImage(render_context.image)

# Scheduler should make sure that the display refreshes every minute and starts refreshing earlier to handle slow display refresh
dashScheduler = DashScheduler(
    [defaultDash],
    render_function=render,
    context=context,
    seconds_in_advance=secondsInAdvance,
    full_clear_interval=clearInterval
)
dashScheduler.start()

