from tkinter import *
from tkinter import ttk

# Colors
color1 = '#1e1f1e' #Black
color2 = '#FEFFFF' #White
color3 = '#38576b' #Blue
color4 = '#272727' #Grey/white
color5 = '#FC7453' #Orange

# Main window
root = Tk()
root.title('Calculator')
root.geometry('235x310')
root.resizable(False,False)
root.config(bg=color1)

# Icon
image_icon = PhotoImage(file = './img/icon.png')
root.iconphoto(False, image_icon)

# Frames
frame_screen = Frame(root, width=235, height=50, bg=color3)
frame_screen.grid(row=0, column=0)

frame_body = Frame(root, width=235, height=260, bg=color1)
frame_body.grid(row=1, column=0)

# Functions
# Handle value input
# eval() is used to handle text strings containing expressions that can be used as data.
all_values = ''

def entry_values(event):
    global all_values
    all_values = all_values + str(event)
    
    # Send the current values to the variable 'all_values'
    text_value.set(all_values)

# Calculate
def calculate():
    global all_values
    result = eval(all_values)
    text_value.set(str(result))

# Clean screen
def clean_screen():
    global all_values
    all_values = ''
    text_value.set('')

# Labels
text_value = StringVar()

screen_label = Label(frame_screen, textvariable=text_value, width=16, height=2, padx=7,
                     relief=RAISED, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=color1, fg=color2)
screen_label.place(x=0, y=0)

# Button
# Row 1
b_1 = Button(frame_body, command= clean_screen, text='C', width=11, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_body, command= lambda:entry_values('%'), text='%', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_body, command= lambda:entry_values('/'), text='/', width=5, height=2, bg=color5, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

# Row 2
b_4 = Button(frame_body, command= lambda:entry_values('7'), text='7', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_body, command= lambda:entry_values('8'), text='8', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_body, command= lambda:entry_values('9'), text='9', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_body, command= lambda:entry_values('*'), text='*', width=5, height=2, bg=color5, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

# Row 3
b_8 = Button(frame_body, command= lambda:entry_values('4'), text='4', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_body, command= lambda:entry_values('5'), text='5', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_body, command= lambda:entry_values('6'), text='6', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_body, command= lambda:entry_values('-'), text='-', width=5, height=2, bg=color5, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

# Row 4
b_12 = Button(frame_body, command= lambda:entry_values('1'), text='1', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_body, command= lambda:entry_values('2'), text='2', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_body, command= lambda:entry_values('3'), text='3', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_body, command= lambda:entry_values('+'), text='+', width=5, height=2, bg=color5, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

# Row 5
b_16 = Button(frame_body, command= lambda:entry_values('0'), text='0', width=11, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_body, command= lambda:entry_values('.'), text='.', width=5, height=2, bg=color4, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_body, command= calculate, text='=', width=5, height=2, bg=color5, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)



root.mainloop()