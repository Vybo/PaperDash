import logging


class FullscreenView:
    def __init__(self, draw, width, height):
        """Initialize the view with a drawing context

        draw - Pillow ImageDraw
        width - Int screen width
        height - Int screen height
        """
        self.draw = draw
        self.width = width
        self.height = height

    def draw_view(self):
        """Will draw the content into the context.
        Must be called every time any property is changed, otherwise changes won't be reflected.

        Overrride in subclasses by calling super().draw_view().
        The super call must be called as the first call in the overriden draw() function, otherwise the order
        will get messed up.

        If done correctly this way, everything will be drawn with a Painters algorithm, thus layered
        from bottom to up properly.
        """
        logging.info('Drawing FullscreenView.')
