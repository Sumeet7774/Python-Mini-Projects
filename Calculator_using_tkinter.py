# Calculator using tkinter

import tkinter as tk 
from tkinter import messagebox as msg

root = tk.Tk()

var1 = tk.StringVar()
var2 = tk.StringVar()


def add():
    num1 = var1.get()
    num2 = var2.get()
    var1.set('')
    var2.set('')
    expression = str(num1) + '+' + str(num2)
    print('The addition is: ',eval(expression))
    msg.showinfo('The addition is: ' , str(eval(expression)))
    
    
def sub():
    num1 = var1.get()
    num2 = var2.get()
    var1.set('')
    var2.set('')
    expression = str(num1) + '-' + str(num2)
    print('The subtraction is: ',eval(expression))
    msg.showinfo('The subtraction is: ' , str(eval(expression)))
    
    
    
def mul():  
    num1 = var1.get()
    num2 = var2.get()
    var1.set('')
    var2.set('')
    expression = str(num1) + '*' + str(num2)
    print('The multiplication is: ',eval(expression))
    msg.showinfo('The multiplication is: ' , str(eval(expression)))
    
    
def div():    
    num1 = var1.get()
    num2 = var2.get()
    var1.set('')
    var2.set('')
    expression = str(num1) + '/' + str(num2)
    print('The division is: ',eval(expression))
    msg.showinfo('The division is: ' , str(eval(expression)))
    
    
label1 = tk.Label(root, text = 'Enter your first number: ') 
entry1 = tk.Entry(root,textvariable = var1)
    
label2 = tk.Label(root,text ='Enter your second number: ')
entry2 = tk.Entry(root,textvariable = var2)
    
button1 = tk.Button(root,text = 'Add',command = add)
button2 = tk.Button(root,text = 'Sub',command = sub)
button3 = tk.Button(root,text = 'Mul',command = mul)
button4 = tk.Button(root,text = 'Div',command = div)
    
    
label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
    
label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
    
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=3,column=0)
button4.grid(row=3,column=1)
    
    
root.mainloop()

