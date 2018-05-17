#!python3
#import sys
#print(sys.version)
#input("Press enter to continue")

from tkinter import *
from tkinter import filedialog
from PIL import Image
import os.path
window = Tk()
window.resizable(0,0)
#indow.resizable(width=false,height=false)
#window.geometry('350x200')
#window.title("make icon file")
#filelbl = Label(window, text="select file to convert to icon")
#filelbl.grid(column=0, row=0)
def filechoose():
    filename = filedialog.askopenfilename(filetypes = (("jpeg files","*.jpg"),("png files", "*.png")))
    if filename == "":
        return
    imgbase = os.path.splitext(filename)[0]
    # imglbl.configure(text=filename)
    img = Image.open(filename)
    imgfull = imgbase + ".ico"
    img.save(imgfull)   
filebtn = Button(window, text="choose image to convert to icon", command=filechoose)
#filebtn.grid(column=1, row=0)
filebtn.pack(padx=10, pady=10)
#imglbl = Label(window, text="...")
#imglbl.grid(column=0, row=1)
window.mainloop()
