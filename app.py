from tkinter import *
from tkinter.ttk import Combobox
import threading
import tkinter.messagebox
import pyshorteners


class short_url:
    def __init__(self,root):
        self.root=root
        self.root.title("Short Url")
        self.root.geometry("500x300")
        self.root.resizable(0,0)
        self.root.iconbitmap("logo591.ico")

        short=StringVar()


        def on_enter(e):
            But_short['background']="black"
            But_short['foreground']="cyan"                              
        def on_leave(e):
            But_short['background']="SystemButtonFace"
            But_short['foreground']="SystemButtonText"



        def on_enters(e):
            But_copy['background']="black"
            But_copy['foreground']="cyan"
        def on_leaves(e):
            But_copy['background']="SystemButtonFace"
            But_copy['foreground']="SystemButtonText"



        def copy():
            self.root.clipboard_clear()
            self.root.clipboard_append(short.get())
            self.root.update()




            
        def short_string():
            try:
                if short.get()!="":
                    url=pyshorteners.Shortener().tinyurl.short(short.get())                    
                    short.set(url)
                else:
                    tkinter.messagebox.showerror('Error',"please enter url")
            except:
                tkinter.messagebox.showerror("Error","Internet connection is not avaiable")



        def thread_short():
            t1=threading.Thread(target=short_string)
            t1.start()

            


        Main_Frame=Frame(self.root,width=500,height=300,bd=6,relief=RIDGE,bg="gray75")
        Main_Frame.place(x=0,y=0)

        Lab_on_top=Label(Main_Frame,text="Paste url in text box to get short form",font=('times new roman',15,'bold'),bg="gray75")
        Lab_on_top.place(x=80,y=0)

        Ent_url=Entry(Main_Frame,width=47,font=('times new roman',14,"bold"),bd=5,textvariable=short)
        Ent_url.place(x=3,y=80)

        But_short=Button(Main_Frame,text="short",font=("times new roman",12,"bold"),bd=4,width=8,height=1,command=thread_short,cursor="hand2")
        But_short.place(x=200,y=160)
        But_short.bind("<Enter>",on_enter)
        But_short.bind("<Leave>",on_leave)

        But_copy=Button(Main_Frame,text="copy to clipboard",font=("times new roman",12,"bold"),bd=4,width=18,height=1,command=copy,cursor="hand2")
        But_copy.place(x=155,y=220)
        But_copy.bind("<Enter>",on_enters)
        But_copy.bind("<Leave>",on_leaves)

if __name__=="__main__":
    root=Tk()
    app=short_url(root)
    root.mainloop()