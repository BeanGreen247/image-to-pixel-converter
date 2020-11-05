# python -m pip install image pillow
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

#img = Image.open('nature01.jpg') 
#filepath="nature01.jpg"
#pixelsize=50
#finalfilepath=""

def pixelate(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )

    image.show()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self, master=None):
        self.label = tk.Label(self)
        self.label["text"] = "type in the pixel size"
        self.label.pack(side="left")

        self.entry = tk.Entry(self)
        self.entry["text"] = "type in the pixel size"
        self.entry.pack(side="left")

        self.conversion = tk.Button(self)
        self.conversion["text"] = "Start"
        self.conversion["command"] = self.startconvert
        self.conversion.pack(side="left")

        self.quit = tk.Button(self, text="exit", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def startconvert(self, master=None):
        filedialogpath = filedialog.askopenfilename(filetypes=(("image files","*.jpg"),("All files","*.*")))
        #self.entry.insert(tk.END, filedialogpath)
        pixelsize=int(self.entry.get())
        pixelate(Path(filedialogpath),pixelsize)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
