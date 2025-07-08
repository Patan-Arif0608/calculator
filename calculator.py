from tkinter import *
import tkinter as tk
mw=Tk()
mw.title("calculator")
e=Entry(mw,width=45,justify=RIGHT)
e.grid(padx=10,pady=10,columnspan=3)
def clear():
    e.delete(0,END)
def btn_click(num):
    a=e.get()
    num1=a+num
    clear()
    e.insert(0,num1)
f1=0
s=''
def calc(s):
    global f1,a1,m
    m=s
    a1=e.get()
    clear()
def equal():
    global f1,s,m
    a2=e.get()
    clear()
    if(m=='+'):
        result=int(a1)+int(a2)
    elif(m=='-'):
        result=int(a1)-int(a2)
    elif(m=='/'):
        result=int(a1)/int(a2)
        result=round(result,4)
    elif(m=='*'):
        result=int(a1)*int(a2)
    e.insert(0,result)
    
    
b1=Button(mw,text='0',padx=36,pady=10,command=lambda:btn_click('0'))
b2=Button(mw,text='1',padx=36,pady=10,command=lambda:btn_click('1'))
b3=Button(mw,text='2',padx=36,pady=10,command=lambda:btn_click('2'))
b4=Button(mw,text='3',padx=36,pady=10,command=lambda:btn_click('3'))
b5=Button(mw,text='4',padx=36,pady=10,command=lambda:btn_click('4'))
b6=Button(mw,text='5',padx=36,pady=10,command=lambda:btn_click('5'))
b7=Button(mw,text='6',padx=36,pady=10,command=lambda:btn_click('6'))
b8=Button(mw,text='7',padx=36,pady=10,command=lambda:btn_click('7'))
b9=Button(mw,text='8',padx=36,pady=10,command=lambda:btn_click('8'))
b10=Button(mw,text='9',padx=36,pady=10,command=lambda:btn_click('9'))
b11=Button(mw,text='+',padx=36,pady=10,command=lambda:calc('+'))
b12=Button(mw,text='-',padx=36,pady=10,command=lambda:calc('-'))
b13=Button(mw,text='/',padx=36,pady=10,command=lambda:calc('/'))
b14=Button(mw,text='*',padx=36,pady=10,command=lambda:calc('*'))
b15=Button(mw,text='=',padx=36,pady=40,command=equal)
b_clr=Button(mw,text='Clear',padx=72,pady=10,command=clear)
b1.grid(row=4,column=0,padx=2,pady=2)
b2.grid(row=3,column=0,padx=2,pady=2)
b3.grid(row=3,column=1,padx=2,pady=2)
b4.grid(row=3,column=2,padx=2,pady=2)
b5.grid(row=2,column=0,padx=2,pady=2)
b6.grid(row=2,column=1,padx=2,pady=2)
b7.grid(row=2,column=2,padx=2,pady=2)
b8.grid(row=1,column=0,padx=2,pady=2)
b9.grid(row=1,column=1,padx=2,pady=2)
b10.grid(row=1,column=2,padx=2,pady=2)
b_clr.grid(row=4,column=1,columnspan=2,padx=2,pady=2)
b11.grid(row=5,column=0,padx=2,pady=2)
b12.grid(row=5,column=1,padx=2,pady=2)
b13.grid(row=6,column=0,padx=2,pady=2)
b14.grid(row=6,column=1,padx=2,pady=2)
b15.grid(row=5,column=2,rowspan=2,padx=2,pady=2)
mw.mainloop()












