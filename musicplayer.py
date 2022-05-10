from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import os
from PIL import Image,ImageTk

# import required module
from playsound import playsound
# for playing note.wav file

root=Tk()
root.title("Music player")
root.after(45)
root.resizable(False,False)
def browse():
    global filename
    filename=fd.askopenfilename(
        initialdir=os.getcwd(),
        title="select a music file",
        filetypes=[('mp3 file','*.mp3'),("all file")]
        )
    basename=os.path.basename(filename)
    dirname=os.path.dirname(filename)
    print(basename,dirname)
    musicname.set(basename)
  
def play():
    try:
        playsound(filename)
        
    except:
        messagebox.showerror("ERROR","NO MUSIC SELECTED")
        
    
        
musicname=StringVar()
musicname.set("../")

print('playing sound using  playsound')
im=Image.open("/harry/Desktop/tkinter_gui/music2.png")
print(im.size)
im=im.resize((300,300))
im=ImageTk.PhotoImage(im)


label=Label(root,bd=4,bg="grey",image=im)
label.grid(row=1,column=0,columnspan=3)
label2=Label(root,text="now playing",font=(20))
label2.grid(row=2,column=0)

label3=Label(root,textvariable=musicname,bd=4,bg="grey",fg="yellow")
label3.grid(row=2,column=1,columnspan=2)


button=Button(root,bd=4,text='browse',command=browse)
button.grid(row=0,column=0)


button_play=Button(root,bd=4,text='play',command=play)
button_play.grid(row=3,column=1)

button2=Button(root,text="stop",command=root.quit)
button2.grid()
root.mainloop()
