from tkinter import *

window=Tk() #this will create the new window
window.configure(background="#847ee0")
window.geometry("312x324") #this wil give the size of the window
window.resizable(0,0) #this will prevent window from resizing
window.title("Calculator") #this wioll give name to that window calculator

#take text from input field
input_text=StringVar()
#------creating fram button inside the window-----------
#creating fram for input values

input_frame=Frame(window,width=300,height=50,borderwidth=3,relief="sunken", highlightbackground="white",highlightcolor="blue",highlightthickness=5)
input_frame.pack(side=TOP,pady=5)

#creating input field inside frame
input_field= Entry(input_frame,font=('arial',20,'bold'),textvariable=input_text,bg="#eee",bd=0,justify=RIGHT,width=18)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)


window.mainloop()