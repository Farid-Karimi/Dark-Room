import customtkinter as ctk
from Image_widgets import *
from PIL import Image, ImageTk
from menu import Menu

class App(ctk.CTk):
	def __init__(self):
		# setup
		super().__init__()
		ctk.set_appearance_mode('dark')
		self.geometry('1000x600')
		self.title('Dark Room')
		self.minsize(800, 500)
		self.init_parameters()

		# layout
		self.rowconfigure(0, weight = 1)
		self.columnconfigure(0, weight = 2, uniform= 'a')
		self.columnconfigure(1, weight = 6, uniform= 'a')

		#canvas data
		self.image_width = 0
		self.image_height = 0
		self.canvas_width = 0
		self.canvas_height = 0
		# widgets
		self.image_import = ImageImport(self, self.import_image)
		# ImportButton (Frame with a button)

		# run
		self.mainloop()

	def init_parameters(self):
		self.rotate_float = ctk.DoubleVar(value = ROTATE_DEFAULT)

		self.rotate_float.trace('w', self.manipulate_image)

	def manipulate_image(self, *args):
		self.image = self.original

		#rotate
		self.image = self.image.rotate(self.rotate_float.get())

		self.place_image()

	def import_image(self, path):
		self.original = Image.open(path)
		self.image = self.original
		self.image_ratio = self.image.size[0] / self.image.size[1]
		self.image_tk = ImageTk.PhotoImage(self.image)

		self.image_import.grid_forget()
		self.image_output = ImageOutput(self, self.resize_image)
		self.close_button = CloseOutput(self,self.close_edit)
		self.menu = Menu(self, self.rotate_float)

	def close_edit(self):
		self.image_output.grid_forget()
		self.close_button.place_forget()
		self.menu.grid_forget()
		self.image_import = ImageImport(self, self.import_image)

	def resize_image(self, event):
		#curr ratio of canvas
		canvas_ratio = event.width / event.height

		#update canvas attributes
		self.canvas_width = event.width
		self.canvas_height = event.height

		#resize
		if canvas_ratio > self.image_ratio:
			self.image_height = int(event.height)
			self.image_width = int(self.image_height * self.image_ratio)
		else:
			self.image_width = int(event.width)
			self.image_height = int(self.image_width / self.image_ratio)

		self.place_image()

	def place_image(self):
		self.image_output.delete('all')
		resized_image = self.image.resize((self.image_width, self.image_height))
		self.image_tk = ImageTk.PhotoImage(resized_image)
		self.image_output.create_image(self.canvas_width/2, self.canvas_width/2, image = self.image_tk)


App()