import customtkinter as ctk
from Settings import *
from tkinter import filedialog, Canvas

class ImageImport(ctk.CTkFrame) :
    def __init__(self, parent, import_func):
        super().__init__(master = parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = 'nsew')
        self.import_func = import_func
        ctk.CTkButton(self, text = 'open image', command = self.open_dialog, hover_color=HOVER, fg_color=BLUE).pack(expand = True)
    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_func(path)


class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(master = parent, background = BACKGROUND, bd = 0, highlightthickness=0, relief='ridge')
        self.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)
        self.bind('<Configure>', resize_image)

class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(master = parent, command=close_func, text = 'x', text_color=WHITE
                         , fg_color='transparent', width=40, height=40
                         ,corner_radius=0, hover_color=CLOSE_RED)
        self.place(relx = 0.99, rely = 0.01, anchor = 'ne')