import datetime

from PIL import Image, ImageFont
from GlobalVariables import *
from dashes.Dash import Dash


class PhotoDash(Dash):
    def __init__(self, context, loader, dash_type, seconds_in_advance):
        self.photo_names = loader.get_all_photo_names()
        self.current_photo_index = 0

        Dash.__init__(self, dash_type, seconds_in_advance)
        self.context = context
        self.loader = loader

        self.font_big = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 48)
        self.font_small = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        self.font_tiny = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 14)
        # self.firebase = client

    def draw_content(self):
        # Fill white over everything
        self.context.draw.rectangle((0, 0, self.context.width, self.context.height), fill=255)
        time = datetime.datetime.now()
        adjusted_time = time - datetime.timedelta(seconds=self.seconds_in_advance)
        formatted_time = adjusted_time.strftime("%H:%M")
        formatted_date = adjusted_time.strftime("%d.%m.%Y")

        # Map
        self.draw_photo()

        # Date & Time
        clock_offset = (self.font_small.size / 4, self.font_small.size / 4)
        date_offset = (clock_offset[0] + 6, clock_offset[1] + self.font_small.size)
        clock_box = (clock_offset[0], clock_offset[1], self.font_tiny.size * 6,
                     date_offset[1] + self.font_small.size)  # ugly ugly ugly

        self.context.draw.rectangle(clock_box, fill=255, outline=0, width=2)
        self.context.draw.text(clock_offset, formatted_time, font=self.font_small, fill=0)
        self.context.draw.text(date_offset, formatted_date, font=self.font_tiny, fill=0)

    def draw_photo(self):
        self.move_photo_index()

        photo_offset = (0, 0)
        photo = self.loader.get_bw_image(self.photo_names[self.current_photo_index])

        new_size = self.calculate_new_size(photo.width, photo.height, self.context.width)
        new_size = round(new_size[0]), round(new_size[1])
        resized_photo = photo.resize(new_size, Image.LANCZOS)
        # cropped_photo = resized_photo.crop(self.calculate_crop_points(self.context.width, self.context.height))

        self.context.image.paste(resized_photo, photo_offset)

    def move_photo_index(self):
        if self.current_photo_index >= len(self.photo_names) - 1:
            self.current_photo_index = 0
        else:
            self.current_photo_index = self.current_photo_index + 1

    def calculate_new_size(self, old_width, old_height, screen_width):
        new_width = screen_width
        new_height = new_width * old_height / old_width

        return (new_width, new_height)

    def calculate_crop_points(self, screen_width, screen_height):
        image_width, image_height = screen_width, screen_height

        # calculate the aspect ratios
        image_aspect_ratio = image_width / image_height
        screen_aspect_ratio = screen_width / screen_height

        if image_aspect_ratio > screen_aspect_ratio:
            # crop the image width to match the screen's aspect ratio
            new_image_width = int(image_height * screen_aspect_ratio)
            width_crop = (image_width - new_image_width) / 2
            crop_points = (width_crop, 0, image_width - width_crop, image_height)
        elif image_aspect_ratio < screen_aspect_ratio:
            # crop the image height to match the screen's aspect ratio
            new_image_height = int(image_width / screen_aspect_ratio)
            height_crop = (image_height - new_image_height) / 2
            crop_points = (0, height_crop, image_width, image_height - height_crop)
        else:
            # no need to crop the image, it already matches the screen's aspect ratio
            crop_points = (0, 0, image_width, image_height)

        return crop_points
