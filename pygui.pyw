from tkinter import *
from tkinter import filedialog
from PIL import Image
import os.path

window = Tk()
window.resizable(0,0)
global sourcename
global destname
global imgfull

sourcelbl = Label(window, text="")
sourcelbl.pack(padx=10, pady=10)
def sourcechoose():
    global sourcename
    sourcename = filedialog.askopenfilename(filetypes = (("image files","*.jpg"), ("image files", "*.png")))
    if sourcename == "":
        return
    sourcelbl.configure(text=sourcename)
sourcebtn = Button(window, text="choose source file", command=sourcechoose)
sourcebtn.pack(padx=10, pady=10)


destlbl = Label(window, text="")
destlbl.pack(padx=10, pady=10)
def destchoose():
   #global sourcename
   global destname
   global imgfull

   destname = filedialog.askdirectory()
   if destname == "":
       return

   imgname = os.path.basename(sourcename)
   imgbase = os.path.splitext(imgname)[0]
   imgext = ".ico"
   imgfull = destname + "/" + imgbase + imgext

   destlbl.configure(text=imgfull)
destbtn = Button(window, text="choose destination directory", command=destchoose)
destbtn.pack(padx=10, pady=10)


def save():
    img = Image.open(sourcename)
    img.save(imgfull)
savebtn = Button(window, text="save", command=save)
savebtn.pack(padx=10,pady=10)

window.mainloop()
