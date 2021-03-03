from tkinter import *
from tkinter import messagebox
from math import *

#=============================================#
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator =""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""
#=============================================#
win = Tk()
win.title("Calculator")

operator = ""
text_input = StringVar()
win.resizable(False,False)

txtDisplay = Entry(win,font=("Arial",20),bg='grey', bd="0", width="26",textvariable=text_input)
txtDisplay.grid(columnspan=4)

#=============================================#
lef = Button(win ,text=("(") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="42" , pady="20" , cursor ='hand2' ,command=lambda:btnClick('(')).grid(row=1 , column=0)
rig = Button(win ,text=(")") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="42" , pady="20" , cursor ='hand2' ,command=lambda:btnClick(')')).grid(row=1 , column=1)
power = Button(win ,text=("^") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="42" , pady="20" , cursor ='hand2',command=lambda:btnClick('**')).grid(row=1 , column=2)
over = Button(win ,text=("%") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="36" , pady="20" , cursor ='hand2' ,command=lambda:btnClick('%')).grid(row=1 , column=3)
#=============================================#
btn9 = Button(win ,text=("9") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="42" , pady="20" , cursor ='hand2', command=lambda:btnClick(9)).grid(row=2 , column=2)
btn8 = Button(win ,text=("8") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="40" , pady="20" , cursor ='hand2', command=lambda:btnClick(8)).grid(row=2 , column=1)
btn7 = Button(win ,text=("7") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="40" , pady="20" , cursor ='hand2', command=lambda:btnClick(7)).grid(row=2 , column=0)
add = Button(win ,text=("+") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="40" , pady="20" , cursor ='hand2' ,command=lambda:btnClick('+')).grid(row=2 , column=3)
#=============================================#
btn4 = Button(win ,text=("4") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="40" , pady="20" , cursor ='hand2', command=lambda:btnClick(4)).grid(row=3 , column=0)
btn5 = Button(win ,text=("5") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="40" , pady="20" , cursor ='hand2', command=lambda:btnClick(5)).grid(row=3 , column=1)
btn6 = Button(win ,text=("6") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="42" , pady="20" , cursor ='hand2', command=lambda:btnClick(6)).grid(row=3 , column=2)
negative = Button(win ,text=("-") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="42" , pady="20" , cursor ='hand2' ,command=lambda:btnClick('-')).grid(row=3 , column=3)
#=============================================#
btn1 = Button(win ,text=("1") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="40" , pady="20" , cursor ='hand2', command=lambda:btnClick(1)).grid(row=4 , column=0)
btn2 = Button(win ,text=("2") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="40" , pady="20" , cursor ='hand2', command=lambda:btnClick(2)).grid(row=4 , column=1)
btn3 = Button(win ,text=("3") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="42" , pady="20" , cursor ='hand2', command=lambda:btnClick(3)).grid(row=4 , column=2)
multiplication = Button(win ,text=("x") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="41" , pady="20" , cursor ='hand2' ,command=lambda:btnClick('*')).grid(row=4 , column=3)
#=============================================#
btn0 = Button(win ,text=("0") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="40" , pady="20" , cursor ='hand2', command=lambda:btnClick(0)).grid(row=5 , column=0)
btnc = Button(win ,text=("c") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="40" , pady="20" , cursor ='hand2', command= btnClearDisplay).grid(row=5 , column=1)
btnm = Button(win ,text=("=") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="42" , pady="20" , cursor ='hand2', command=btnEqualsInput).grid(row=5 , column=2)
multiplication = Button(win ,text=("/") , font=("Arial",16) , bg="green" ,fg="white", activebackground="yellow" , activeforeground="black" , padx="42" , pady="20" , cursor ='hand2' , command=lambda:btnClick('/')).grid(row=5 , column=3)


def about():
    messagebox.showinfo('about' , '  ساخته شد است  Mr Hidden این ابزار توسط \n Telegram : @Hidden0612\nVersion : 1.0')

def helps():
    messagebox.showinfo('Help' , 'برای دانلود پست ها کافیه فقط لینک پست را به ابزار بدین\n Version : 1.0')

menubar = Menu(win)
win.config(menu = menubar)

menubar.add_cascade(label = 'Help' , command = helps)
menubar.add_cascade(label = 'About' , command = about)
menubar.add_cascade(label = 'Exit' , command = win.destroy)
win.mainloop()