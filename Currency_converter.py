
'''Currency Converter

first install a pip for converting currencies
and tkinter For GUI '''

from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import ttk
a=CurrencyConverter()                         # 'a' is are currency converter, we deifne it
PK_Exch_Rate=0.00437
root = tk.Tk()
root.geometry("500x360")
root.title("Currency Converter")

#this for button command function.
def clicked():
    amount=eval(e1.get())           #we store are e1 value in amount variable
    cur1=e2.get()                   #we store are currency in e2, now for the conversion we store it in a variable 
    cur2=e3.get()                   #we store are Required currency in e3, now for the conversion we store it in a variable 
    if cur1 == 'PKR':
        data=amount*PK_Exch_Rate
    elif cur2 == 'PKR':
        data = amount/PK_Exch_Rate
    else:
        data=a.convert(amount,cur1,cur2)
    l4=tk.Label(root,text=data,font= "Times 10 bold").place(x=100,  y=285)
    #we create a label to insert the datain l4[text=], here comes the converted value of the currency 

        

#this whole work is for GUI:

#Here we are going to add a label in our application for entering the amount
l1=tk.Label(root,text="Enter amount here: ",font= "Times 10 bold").place(x=50, y=80)
#now we have to create a enrty a widget,the .Entry() provide the single line text box to the user.this is for l1
e1=tk.Entry(root) 

#now we have to create a currency label, and a enrty widget for l2
l2=tk.Label(root,text="Enter Currency: ",font= "Times 10 bold").place(x=50, y=130)
e2=tk.Entry(root)

#now we have to create a converted currency label , and enrty widget for l3
l3=tk.Label(root,text="Enter Required Currency: ",font= "Times 10 bold").place(x=50, y=180)
e3=tk.Entry(root)

#now we have to create a button, when we click it, we get output
b=tk.Button(root,text="Click",command=clicked).place(x=230, y=235)
e1.place(x=200, y=85)
e2.place(x=200, y=135)
e3.place(x=200, y=185)


root.mainloop()


    
    
    
    
    
    
    
    
    
    
    
#a=CurrencyConverter()                              # we are calling the functuon of currency converter in 'a' 
#print(a.convert(12,"Rupees","USD"))