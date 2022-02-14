from tkinter import *
import sys

window=Tk() #this will create the new window
window.configure(background="#E3EBEA")
window.geometry("312x440") #this wil give the size of the window
window.resizable(0,0) #this will prevent window from resizing
window.title("Calculator") #this wioll give name to that window calculator
#--------------------addding functions to the buttons created------------
#btn_click function

def btn_click(key):
	Terror.delete('1.0', END)
	global expresion  
	if len(expresion)<=15:
		print(len(expresion))
		expresion = expresion+str(key)
		input_text.set(expresion)
	else:
		input_text.set(expresion)
		Terror.insert(END,"Limit crossed ")


'''def btn_delete():
	global expresion
	expresion.delete(0, END)'''
def btn_delete():
	global expresion
	expresion = expresion[0:len(expresion) -1]
	input_text.set(expresion)

def btn_delete():
	Terror.delete('1.0', END)
	global expresion
	expresion = expresion[:-1]
	input_text.set(expresion)

def bt_clear():
	Terror.delete('1.0', END)
	global expresion
	expresion = ""
	input_text.set(expresion)

def bt_qual():
	global expresion
	try:
		Terror.delete('1.0', END)
		result=str(round(eval(expresion),5))
		input_text.set(result)
		expresion=result
	except SyntaxError as SEr:
		Terror.insert(END,"Invalide Input ")
		print(SEr)
		expresion=""
	except ZeroDivisionError as ZEr:
		Terror.insert(END,"Undefined ( Can not divide by zero :| )")
		print(ZEr)



expresion=""
#take text from input field
input_text=StringVar()


#------creating frame for input values-------

input_frame=Frame(window,width=300,height=50,borderwidth=3,relief="sunken", highlightbackground="white",highlightcolor="white",highlightthickness=5)
input_frame.pack(side=TOP,pady=5)

#creating input field inside frame
input_field= Entry(input_frame,font=('arial',20,'bold'),textvariable=input_text,bg="#eee",bd=0,justify=RIGHT,width=18)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)
#-------------------------------------
#adding error screen/frame
#error_frame=Frame(window,width=290,height=50,bg="#2F3033")
#error_frame.pack(pady=2,padx=2) 

#error text field
Terror=Text(window,width=40,height=1,bg="#2F3033",fg="#E3EBEA")
Terror.configure(font=("Courier", 9, "italic"))
Terror.pack()

#__________________________________
#let us creat a frame for buttons(numbers/operator/equalsymble

btn_frame=Frame(window,width=312,height=272.5,bg="#E3EBEA")
btn_frame.pack()

#adding button to the frame
#first row
clear=Button(btn_frame,text="C",bg="#6A63A0",fg="#E3EBEA",width=30,height=3,bd=0,cursor="hand2",command=lambda:bt_clear())
clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)

divide=Button(btn_frame,text="/",width=9,height=3,bd=0,bg="#6A63A0",fg="#E3EBEA",cursor="hand2",command=lambda:btn_click("/"))
divide.grid(row=0,column=3,padx=1,pady=1)

#secondrow

seven=Button(btn_frame,text="7",width=9,height=3,bg="#4F4860",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click("7"))
seven.grid(row=1,column=0,padx=1,pady=1)
eight=Button(btn_frame,text="8",width=9,height=3,bg="#4F4860",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click("8"))
eight.grid(row=1,column=1,padx=1,pady=1)
nine=Button(btn_frame,text="9",width=9,height=3,bg="#4F4860",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click("9"))
nine.grid(row=1,column=2,padx=1,pady=1)
multiply=Button(btn_frame,text="*",width=9,height=3,bg="#6A63A0",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click("*"))
multiply.grid(row=1,column=3,padx=1,pady=1)

#third row

four=Button(btn_frame,text="4",width=9,height=3,bg="#4F4860",bd=0,fg="#E3EBEA",cursor="hand2",command=lambda :btn_click(4))
four.grid(row=2,column=0,padx=1,pady=1)
five=Button(btn_frame,text="5",width=9,height=3,bg="#4F4860",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click(5))
five.grid(row=2,column=1,padx=1,pady=1)
five=Button(btn_frame,text="6",width=9,height=3,bg="#4F4860",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click(6))
five.grid(row=2,column=2,padx=1,pady=1)
substract=Button(btn_frame,text="-",width=9,height=3,bg="#6A63A0",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click("-"))
substract.grid(row=2,column=3,padx=1,pady=1)

#fourth row

one=Button(btn_frame,text="1",width=9,height=3,bg="#4F4860",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click(1))
one.grid(row=3,column=0,padx=1,pady=1)
two=Button(btn_frame,text="2",width=9,height=3,bg="#4F4860",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click(2))
two.grid(row=3,column=1,padx=1,pady=1)
three=Button(btn_frame,text="3",width=9,height=3,bg="#4F4860",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click(3))
three.grid(row=3,column=2,padx=1,pady=1)
add=Button(btn_frame,text="+",width=9,height=3,bg="#6A63A0",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda :btn_click("+"))
add.grid(row=3,column=3,padx=1,pady=1)

#fifth row

zero=Button(btn_frame,text="0",width=20,height=3,bg="#4F4860",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda: btn_click(0))
zero.grid(row=4,column=0,padx=1,pady=1,columnspan=2)
point=Button(btn_frame,text=".",width=9,height=3,bg="#6A63A0",bd=0,fg="#E3EBEA",cursor="hand2",command=lambda: btn_click("."))
point.grid(row=4,column=2,padx=1,pady=1)
equal=Button(btn_frame,text="=",width=9,height=3,bg="#a0637a",bd=0,fg="#E3EBEA",cursor="hand2",command=lambda: bt_qual())
equal.grid(row=4,column=3,padx=1,pady=1)

#sixth row
photo = PhotoImage(file = "backspace.png")
delete=Button(btn_frame,width=145,height=50,bg="#6A63A0",fg="#E3EBEA",bd=0,cursor="hand2",command=lambda: btn_delete(),image=photo)
delete.grid(row=5,column=2,padx=1,pady=1,columnspan=2)
openb=Button(btn_frame,text="(",width=9,height=3,bg="#6A63A0",bd=0,fg="#E3EBEA",cursor="hand2",command=lambda: btn_click("("))
openb.grid(row=5,column=0,padx=1,pady=1)
closeb=Button(btn_frame,text=")",width=9,height=3,bg="#6A63A0",bd=0,fg="#E3EBEA",cursor="hand2",command=lambda: btn_click(")"))
closeb.grid(row=5,column=1,padx=1,pady=1)


window.mainloop()
