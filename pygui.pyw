from tkinter import *
from tkinter import filedialog
from PIL import Image
import os.path
window = Tk()
window.resizable(0,0)

def sourcechoose():
    #filename = filedialog.askopenfilename(filetypes = (("jpeg files","*.jpg"),("png files", "*.png")))
    sourcename = filedialog.askopenfilename(filetypes = (("image files","*.jpg"), ("image files", "*.png")))
    if sourcename == "":
        return
    #imgbase = os.path.splitext(sourcename)[0]
    #return filename
    #img = Image.open(filename)
    #imgfull = imgbase + ".ico"
    #img.save(imgfull)

sourcebtn = Button(window, text="choose source file", command=sourcechoose)
sourcebtn.pack(padx=10, pady=10)

#def destchoose():
#    #filename = filedialog.askopenfilename(filetypes = (("jpeg files","*.jpg"),("png files", "*.png")))
#    global destname = filedialog.askdirectory()
#    if destname == "":
#        return
#
#    imgname = os.path.basename(sourcename)
#    imgbase = os.path.splitext(imgname)[0]
#    imgext = ".ico"
#    imgfull = destname + imgbase + imgext
#
#    img = Image.open(sourcename)
#    img.save(imgfull)
#destbtn = Button(window, text="choose destination directory", command=destchoose)
#destbtn.pack(padx=10, pady=10)


window.mainloop()
