from dataclasses import replace
from encodings import utf_8
from gettext import find
from hashlib import new
import tkinter as tk
from tkinter import LEFT, PhotoImage, ttk
from tkinter import colorchooser, font, messagebox
import os
from tkinter import filedialog
from turtle import end_poly, pos
from click import command
from matplotlib.ft2font import BOLD
from matplotlib.pyplot import get

from numpy import character, save

main_window = tk.Tk()
main_window.geometry("1200x800")
main_window.title("X")
#-------------main menu-----------------------------#
main_menu = tk.Menu()

#Icons
#file icons
new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
save_as_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")
#Edit icon
copy_icon = tk.PhotoImage(file="icons2/copy.png")
paste_icon = tk.PhotoImage(file="icons2/paste.png")
cut_icon = tk.PhotoImage(file="icons2/cut.png")
clear_all_icon = tk.PhotoImage(file="icons2/clear_all.png")
find_icon = tk.PhotoImage(file="icons2/find.png")
#View icons
tool_bar_icon = tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon = tk.PhotoImage(file="icons2/status_bar.png")
#Theme icons
light_default_icon = tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon = tk.PhotoImage(file="icons2/light_plus.png")
dark_icon = tk.PhotoImage(file="icons2/dark.png")
red_icon = tk.PhotoImage(file="icons2/red.png")
monokai_icon = tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon = tk.PhotoImage(file="icons2/night_blue.png")

#menu
file = tk.Menu(main_menu, tearoff=False)
edit = tk.Menu(main_menu, tearoff=False)
view = tk.Menu(main_menu, tearoff=False)
theme = tk.Menu(main_menu, tearoff=False)







# cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Theme', menu=theme)

#-------------main menu end-------------------------#


#--------------toolbar------------------------------#

tool_bar = ttk.Label(main_window)
tool_bar.pack(side=tk.TOP, fill = tk.X)

#font box
font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family)
font_box['values'] = font_tuples
font_box.current(2)
font_box.grid(row=0, column=0, padx=5)

#size box
size_var = tk.IntVar()
size_box = ttk.Combobox(tool_bar, width=5, textvariable=size_var)
size_box['values'] = tuple(range(4,100))
size_box.current(7)
size_box.grid(row=0, column=1, padx=5)

# bold button
bold_icon = tk.PhotoImage(file="icons2/bold.png")
bold_button = ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row = 0, column=2, padx=5)
#italic button
italic_icon = tk.PhotoImage(file="icons2/italic.png")
italic_button = ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=3, padx=5)
#under line button
underline_icon = tk.PhotoImage(file="icons2/underline.png")
underline_button = ttk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0, column=4, padx=5)
#font colour button
font_color_icon = tk.PhotoImage(file="icons2/font_color.png")
font_color_button = ttk.Button(tool_bar, image=font_color_icon)
font_color_button.grid(row=0, column=5, padx=5)
#left align
left_align_icon = tk.PhotoImage(file="icons2/align_left.png")
left_align_button = ttk.Button(tool_bar, image=left_align_icon)
left_align_button.grid(row=0, column=6, padx= 5)
#center align
center_align_icon = tk.PhotoImage(file="icons2/align_center.png")
center_align_button = ttk.Button(tool_bar, image=center_align_icon)
center_align_button.grid(row=0, column=7, padx= 5)
#right align
right_align_icon = tk.PhotoImage(file="icons2/align_right.png")
right_align_button = ttk.Button(tool_bar, image=right_align_icon)
right_align_button.grid(row=0, column=8, padx= 5)
#--------------toolbar end--------------------------#

#-------------text editor---------------------------#
text_editor = tk.Text(main_window)
text_editor.config(wrap='word', relief=tk.FLAT)

#scroll bar
scroll_bar = tk.Scrollbar(main_window)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)

scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and font size functionality

current_font_family = "Lohit Kannada"
current_font_size = 11
def change_font(main_window):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))
def change_font_size(main_window):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))
font_box.bind("<<ComboboxSelected>>", change_font)
size_box.bind("<<ComboboxSelected>>", change_font_size)

#-------------------Button Functionality----------------#
#bold button
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, "bold"))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))
bold_button.configure(command=change_bold)

#italic button
def change_italic():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, "italic"))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size, "normal"))
italic_button.configure(command=change_italic)

#under button
def change_underline():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
underline_button.configure(command=change_underline)

#font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_button.configure(command=change_font_color)

#align functaionality
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
def align_center():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
def align_right():
    text_content = text_editor.get(1.0,"end")
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
left_align_button.configure(command=align_left)
center_align_button.configure(command=align_center)
right_align_button.configure(command=align_right)

text_editor.config(font=("Lohit Kannada",11))
#-------------text editor end-----------------------#
#------------- Status Bar---------------------------#
status_bar = ttk.Label(main_window, text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event = None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f"Characters : {characters} Words : {words}")
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>', changed)
#------------- Status Bar Ended---------------------#
#--------------main menu function-------------------#
# variable
url = ''
#new functionality
def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)
#open functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(('Text File', '*.txt'),('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_window.title(os.path.basename(url))
#save functionality
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding=utf_8) as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text File', '*.txt'),('All files', '*.*')))
            file_content = text_editor.get(1.0, tk.END)
            url.write(file_content)
            url.close()
    except:
        return
# save as functionality
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url  =filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text File', '*.txt'),('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return
#exit functionality
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url,'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_window.destroy()
                else:
                    content =str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text File', '*.txt'),('All files', '*.*')))
                    url.write(content)
                    url.close()
                    main_window.destroy()
            elif mbox is False:
                main_window.destroy()
            else:
                pass
        else:
            main_window.destroy()
    except:
        return
# find functionality
def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                
    def replace():
        pass
    find_dialog = tk.Toplevel()
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)
    #frame
    find_frame = ttk.LabelFrame(find_dialog, text='Find/Replace')
    find_frame.pack(pady=20)
    #label
    text_find_label = ttk.Label(find_frame, text='Find :')
    text_replace_label = ttk.Label(find_frame, text="Replace")

    #entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    #button
    find_button = ttk.Button(find_frame, text="Find", command=find)
    replace_button = ttk.Button(find_frame, text="Replace",command=replace)

    #label grid
    text_find_label.grid(row = 0, column = 0, padx=4, pady=4)
    text_replace_label.grid(row = 1, column=0, padx=4, pady=4)

    #entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    #button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialog.mainloop()
#file command
file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N", command=new_file)
file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O", command=open_file)
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S", command=save_file)
file.add_command(label="Save As", image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S", command=save_as)
file.add_separator() 
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q", command=exit_func)
#Edit drop down command
edit.add_command(label="Copy", image=copy_icon, accelerator="Ctrl+C", compound=tk.LEFT, command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X", command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+C", command=lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F", command=find_func)
#View drop down
view.add_checkbutton(label="Tool Bar", image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label="Status Bar", image=status_bar_icon, compound=tk.LEFT)
#Theme Drop Down 
theme.add_radiobutton(label="Ligh Default", image=light_default_icon, compound=tk.LEFT)
theme.add_radiobutton(label="Light Plus", image=light_plus_icon, compound=tk.LEFT)
theme.add_radiobutton(label="Dark", image=dark_icon, compound=tk.LEFT)
theme.add_radiobutton(label="Red", image=red_icon, compound=tk.LEFT)
theme.add_radiobutton(label="Monokai", image=monokai_icon, compound=tk.LEFT)
theme.add_radiobutton(label="Night Blue", image=night_blue_icon, compound=tk.LEFT)
theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' : ('#ededed', '#6b9c2')
}
count = 0
#--------------end main menu function---------------#
main_window.config(menu=main_menu)
main_window.mainloop()