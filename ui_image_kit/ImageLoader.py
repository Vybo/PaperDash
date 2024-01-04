from PIL import Image
import os

class ImageLoader:
    def __init__(self, resources_directory):
        self.directory = resources_directory

    def get_bw_image(self, name):
        image = Image.open(self.directory + '/' + name)  # open colour image
        image = self.remove_transparency(image).convert('L')  # convert image to black and white
        return image

    def get_all_photo_names(self):
        return [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]

    def remove_transparency(self, image, bg_colour=(255, 255, 255)):
        # Only process if image has transparency
        if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):

            # Need to convert to RGBA if LA format due to a bug in PIL
            alpha = image.convert('RGBA').split()[-1]

            # Create a new background image of our matt color.
            # Must be RGBA because paste requires both images have the same format

            bg = Image.new("RGBA", image.size, bg_colour + (255,))
            bg.paste(image, mask=alpha)
            return bg

        else:
            return image
