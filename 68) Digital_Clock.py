# Digital_Clock

from tkinter import * # type: ignore

# tkinter is the standard GUI (Graphical User Interface) library in Python.
# It provides a way to create windows, dialogs, and various GUI elements like buttons, labels, text boxes, etc.
# We are using it to create a dialog or textbox

from time import strftime
# it will import these
#  %Y Year with century as a decimal number.
#  %m Month as a decimal number [01,12].
#  %d Day of the month as a decimal number [01,31].
#  %H Hour (24-hour clock) as a decimal number [00,23].
#  %M Minute as a decimal number [00,59].
#  %S Second as a decimal number [00,61].

# Creating a window or dialog for our clock

window = Tk()
time_label = Label(window,font = ("Arial",50),fg ="white",bg = "black")
time_label.pack()

def update_time():
    time_string = strftime("%I:%M:%S %p") #For time
    time_label.config(text=time_string)

    day_string = strftime("%A") #For day
    day_label.config(text= day_string)

    date_string = strftime("%B %d:%Y")
    date_label.config(text = date_string)

    window.after(1000,update_time) #update the time in every mili sec


day_label = Label(window,font = ("Arial",40))
day_label.pack()

date_label = Label(window,font =("Arial",50))
date_label.pack()

update_time()
window.mainloop()