class Context:
    def __init__(self, image, draw, width, height):
        self.image = image
        self.draw = draw
        self.width = width
        self.height = height


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect:
    def __init__(self, origin, size):
        self.origin = origin
        self.size = size
