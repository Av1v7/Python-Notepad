# ************************************
# Python Text Editor
# ************************************
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

# Define Things
def change_color():
    color = colorchooser.askcolor(title="Pick A Color.")
    text_area.config(fg=color[1])
    showinfo("Success !", f"You Have Successfully Changed Color.\nColor ID: {color}")

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))
    showinfo("Success !", f"You Have Successfully Changed Font.")

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)
    
    print("Successfully created file.")
    showinfo("Success !", "You have Successfully created a new file.")

def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])
    
    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")
            text_area.insert(1.0, file.read())
            file.close()
            print("Successfully opened file.")
            showinfo("Success !", "Open This .txt File Was Successfully Done.")

        except Exception:
            print("couldn't read file")

def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.close()
            file.write(text_area.get(1.0, END))
            
            print("Successfully saved file.")
            showinfo("Success !", "Save This .txt File Was Successfully Done.")
            
        except Exception:
            print("couldn't save file")

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def select_all():
    text_area.event_generate("<<SelectAll>>")

def about():
    showinfo("About This Program", "This is a program written by Av1v, Hope you will enjoy.")

def quit():
    window.destroy()
    print("Exit Successfully")


window = Tk()
window.title("Text Editor Program.")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Define icon to my application
window.iconbitmap('text_editor.ico')
# Define icon to my application


font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)


frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0,column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

# File Menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# Edit Menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

# Help Menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Button for closing
close_window_button = Button(window, text= "Close the Window", font=("Calibri", 10,"bold"), command=quit)
close_window_button.grid(row=2, column=0)

window.mainloop()