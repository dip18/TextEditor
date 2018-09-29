from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import datetime

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

# When click on word count
def word_count():
    total_text = textBox.get(1.0, END)
    word_list = total_text.split()
    no_of_words = len(word_list)
    messagebox.showinfo('Word Count', 'Total no of Words ' + str(no_of_words))    
    
# When click on Date/Time
def date_time():
    now = datetime.datetime.now()
    d_t = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    textBox.insert(END, d_t)

# When click on Find
def main_find():
    child1 = Tk()
    child1.title("Find Word")
    child1.geometry('350x70')
    
    def cancel():                    #Cancel method under Find
        child1.destroy()
    
    def find():                      #Find method under Find
        total_text = textBox.get(1.0, END)
        word_list = total_text.split()
        input_text = inputText.get()
        word_index = []
        for index, word in enumerate(word_list):
            if word == input_text:
                word_index.append(index)
        if len(word_index) > 0:
            no_of_found = len(word_index)
            messagebox.showinfo('Total Found', 'Total no of the word : ' + '" ' + input_text + ' "' + ' is found ' + str(no_of_found) + ' times')
            child1.destroy()
        else:
            messagebox.showerror("Error", "Not Found")
            child1.destroy()                        
        
    label = Label(child1, width=20, height=2, text="Find Word", anchor='w').grid(row=0)
    inputText = Entry(child1, width=30)
    inputText.grid(row=0, column=1)
    button1 = Button(child1, text="Find", width=10, command=find).grid(row=2, column=0, sticky=W, pady=4)
    button2 = Button(child1, text="Cancel", width=10, command=cancel).grid(row=2, column=1, sticky=W, pady=4)
    child1.mainloop()

# When click on Replace
def main_replace():
    child2 = Tk()
    child2.title("Replace Word")
    
    def cancel():                    #Cancel method under Replace
        child2.destroy()
    
    def replace():                      #Find method under Replace
        total_text = textBox.get(1.0, END) 
        input_text1 = inputText1.get()
        input_text2 = inputText2.get()    
        new_text = total_text.replace(input_text1, input_text2)
        textBox.delete(1.0, END)
        textBox.insert(END, new_text)
        child2.destroy()         
        
    label1 = Label(child2, width=20, height=2, text="Old Word", anchor='w').grid(row=0)
    label2 = Label(child2, width=20, height=2, text="Replace Word", anchor='w').grid(row=1)
    inputText1 = Entry(child2, width=30)
    inputText2 = Entry(child2, width=30)
    inputText1.grid(row=0, column=1)
    inputText2.grid(row=1, column=1)
    button1 = Button(child2, text="Replace", width=10, height=2, command=replace).grid(row=3, column=0, sticky=W, pady=4)
    button2 = Button(child2, text="Cancel", width=10, height=2, command=cancel).grid(row=3, column=1, sticky=W, pady=4)
    child2.mainloop()

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
editmenu.add_command(label="Find Word", command=main_find, accelerator="Ctrl+F")
editmenu.add_command(label="Replace Word", command=main_replace, accelerator="Ctrl+R")
editmenu.add_separator()
editmenu.add_command(label="Date/Time", command=date_time)
menubar.add_cascade(label="Edit", menu=editmenu)
        
#The Tools Menu
toolmenu = Menu(menubar, tearoff=0)
toolmenu.add_command(label="Word Count", command=word_count, accelerator="Ctrl+W")
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