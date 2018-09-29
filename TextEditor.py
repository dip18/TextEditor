from tkinter import *
import tkinter.messagebox
import tkinter.filedialog

# When click on New
def newDocu():
    result = tkinter.messagebox.askquestion("Text Editor", "Do you want to save changes?")
    if result == "Yes":
        saveAsDocu()
    else:
        textBox.delete(1.0, END)
            
# When click on SaveAs
def saveAsDocu():
    global filename
    filepath = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if filepath is None:
        return
    save = str(textBox.get(1.0, END))
    filepath.write(save)
    filename = filepath.name
    filepath.close()

# When click on Save
def saveDocu():
    global filename
    if (filename == ''):
        saveAsDocu()
    else:
        save_file = open(filename, 'w')
        save1 = str(textBox.get(1.0, END))
        save_file.write(save1)
        filename = save_file.name
        save_file.close()

# When click on Open
def openDocu():
    openfile = tkinter.filedialog.askopenfile(mode='r')
    alltext = openfile.read()
    textBox.insert(END, alltext)
    openfile.close()

# When click on Clear all
def clearDocu():
    textBox.delete(1.0, END)

# When click on Exit
def exitDocu():
    root.destroy()

# When click on Undo
def undoDocu():
    textBox.event_generate("<<Undo>>")

# When click on Redo
def redoDocu():
    textBox.event_generate("<<Redo>>")

# When click on Cut
def cutDocu():
    textBox.event_generate("<<Cut>>")

# When click on Copy
def copyDocu():
    textBox.event_generate("<<Copy>>")

# When click on Paste
def pasteDocu():
    textBox.event_generate("<<Paste>>")

# When click on Select All
def selectallDocu():
    textBox.tag_add('sel', 1.0, END)

# When Right click
def popup(event):
    try:
        popupmenu.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popupmenu.grab_release()

# When Press the 'X' button
def on_closing():
    if messagebox.askokcancel("Text Editor", "Do you want to quit?"):
        root.destroy()


#TextBox Creation
root = Tk()
textBox=Text(root)
textBox.pack(expand=YES, fill=BOTH)
textBox.bind("<Button-3>", popup)
filename = ''
        
#The File Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newDocu, accelerator="Ctrl+N")
filemenu.add_command(label="Open",command=openDocu, accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=saveDocu, accelerator="Ctrl+S")
filemenu.add_command(label="Save as...", command=saveAsDocu)
filemenu.add_command(label="Clear All", command=clearDocu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitDocu)
menubar.add_cascade(label="File", menu=filemenu)
        
#The Edit Menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=undoDocu, accelerator="Ctrl+Z")
editmenu.add_command(label="Redo", command=redoDocu, accelerator="Ctrl+Y")
editmenu.add_separator()
editmenu.add_command(label="Cut", command=cutDocu, accelerator="Ctrl+X")
editmenu.add_command(label="Copy", command=copyDocu, accelerator="Ctrl+C")
editmenu.add_command(label="Paste", command=pasteDocu, accelerator="Ctrl+V")
editmenu.add_separator()
editmenu.add_command(label="Select All", command=selectallDocu, accelerator="Ctrl+A")
menubar.add_cascade(label="Edit", menu=editmenu)
        
#The Tools Menu
toolmenu = Menu(menubar, tearoff=0)
toolmenu.add_command(label="Word Count", accelerator="Ctrl+W")
menubar.add_cascade(label="Tool", menu=toolmenu)

#Right Click menu
popupmenu = Menu(root, tearoff=0)
popupmenu.add_command(label="Undo", command=undoDocu)
popupmenu.add_command(label="Redo", command=redoDocu)
popupmenu.add_separator()
popupmenu.add_command(label="Cut", command=cutDocu)
popupmenu.add_command(label="Copy", command=copyDocu)
popupmenu.add_command(label="Paste", command=pasteDocu)
popupmenu.add_separator()
popupmenu.add_command(label="Select All", command=selectallDocu)       
root.config(menu=menubar)

root.title('Text Editor')
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()