import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, rotation):
        super().__init__(master = parent)
        self.grid(row = 0, column = 0, sticky = 'nsew', pady = 10, padx = 10)

        self.add('Position')
        self.add('Color')
        self.add('Effects')
        self.add('Export')

        PositionFrame(self.tab('Position'), rotation)
        ColorFrame(self.tab('Color'))


class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, rotation):
        super().__init__(master = parent, fg_color='transparent')
        self.pack(expand = True, fill = 'both')
        SliderPanel(self, 'Rotation', rotation, 0, 360)
        # SliderPanel(self, 'Zoom')

class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color='transparent')
        self.pack(expand = True, fill = 'both')
