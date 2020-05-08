from tkinter import Frame as tkFrame
from tkinter import Canvas as tkCanvas
from tkinter import *
from PIL import ImageTk, Image


class TkinkerRenderer:
    def __init__(self, window_height, window_width):
        self.windowRoot = Tk(className='PyDash - Window mode')
        self.windowRoot.geometry("{}x{}".format(window_width, window_height))
        self.canvas = tkCanvas(master=self.windowRoot, width=window_width, height=window_height)
        self.windowRoot.update()

    def renderImage(self, image):
        image_tk = ImageTk.PhotoImage(image)
        img_item = self.canvas.create_image(0, 0, anchor=NW, image=image_tk)
        self.canvas.pack()
        self.windowRoot.update()

