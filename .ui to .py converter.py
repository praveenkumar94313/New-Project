from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
def main():
    def ask():
        #asking for file type and file to convert into .py
        try:

            global  askdir
            filename= filedialog.askopenfile(initialdir="/",title="select a file",filetype=(("UI","*.ui"),("All Files","*.*")))
            dir.set(filename.name)
            askdir=filename.name
            return root
        except :
            messagebox.showerror("Error", "An Error Has Been Occured")

    def save():
        #asking for name of the file and directory of the file
        try:
            global nm
            global savedir,t
            inp = dir3.get()
            if inp==" " or inp=="":
                messagebox.showerror("Error","Enter A Valid Name")
            else:
                nm=""
                if ".py" in inp:
                    pass
                else:
                    inp=inp+".py"
                for i in range(len(inp)):
                    if " " in inp:
                        nm=inp.replace(" ","_")
                    else:
                        nm=inp
                filename1 = filedialog.askdirectory(initialdir="/",title="Save As")
                t=filename1
                return root
        except:
            messagebox.showerror("Error", "An Error Has Been Occured")

    def convert():
        #converting ui to .py
        try:
            import os
            import shutil
            import subprocess
            import time
            inp = dir3.get()
            if ".py" in inp:
                pass
            else:
                inp = inp + ".py"
            for i in range(len(inp)):
                if " " in inp:
                    nm = inp.replace(" ", "_")
                else:
                    nm = inp
            o = askdir
            s = o.split("/")
            ty = s[-1]
            nm1 = ""
            for i in range(len(ty)):
                if " " in ty:
                    nm1 = ty.replace(" ", "_")
                else:
                    nm1 = ty
            s1 = ""
            s2 = ""
            for i in range(1, len(s) - 1):
                s1 = s1 + "\\" + s[i]
            for i in range(1, len(s) - 1):
                s2 = s2 + "/" + s[i]
            real1 = "C:" + s1 + "/%s" % (ty)
            real = "C:" + s1 + "/%s" % (nm1)
            real2 = "C:" + s2 + "/%s" % (nm)
            if " " in ty:
                os.rename(real1, real)
            s1 = "cd C:" + s1 + " & pyuic5 -x " + nm1 + " -o " + nm
            sfinal = 'cmd /k "%s"' % (s1)
            subprocess.Popen(sfinal)
            time.sleep(2)
            t1=t+"/"+nm
            sor="C:"+s2
            source=r"%s"%(sor)
            destination = r"%s" % (t)
            shutil.move(real2,t1)
        except:
            messagebox.showerror("Error", "An Error Has Been Occured")
    try:
        root = Tk()
        root.geometry("457x111")
        root.title("Convert PyQt5 To Python File")
        label1=Label(root,text="Choose PyQt5 File To Convert",background="red",relief=SUNKEN,font="Ariel 13 normal",width=39,bd=3)
        label1.place(x=0,y=0)
        button = Button(root,text="Select",command=ask,font="Ariel 10 normal")
        button.place(x=310,y=28)
        dir=StringVar()
        entry1=Entry(root,textvariable=dir,state=DISABLED,width=50,relief=SUNKEN,bd=5)
        dir.set("")
        entry1.place(x=0,y=28)
        label3=Label(root,text="Enter File Name",background="red",relief=SUNKEN,font="Ariel 13 normal",width=39,bd=3)
        label3.place(x=0,y=55)
        button1 = Button(root,text="Submit",command=save,font="Ariel 10 normal")
        button1.place(x=310,y=83)
        dir3=StringVar()
        entry3=Entry(root,textvariable=dir3,width=50,relief=SUNKEN,bd=5)
        entry3.place(x=0,y=83)
        convertbutton = Button(root,text="CONVERT",command=convert,font="Ariel 12 bold",height=5,relief=GROOVE, bd=5)
        convertbutton.place(x=359,y=0)
        root.mainloop()
    except:
        messagebox.showerror("Error", "An Error Has Been Occured")


if __name__ == "__main__":
    main()
