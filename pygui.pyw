from tkinter import *
from tkinter import filedialog
from PIL import Image
import os.path
window = Tk()
window.resizable(0,0)
def filechoose():
    filename = filedialog.askopenfilename(filetypes = (("jpeg files","*.jpg"),("png files", "*.png")))
    if filename == "":
        return
    imgbase = os.path.splitext(filename)[0]
    img = Image.open(filename)
    imgfull = imgbase + ".ico"
    img.save(imgfull)   
filebtn = Button(window, text="choose image to convert to icon", command=filechoose)
filebtn.pack(padx=10, pady=10)
window.mainloop()
