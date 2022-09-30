import tkinter as tk
from tkinter import messagebox
from functools import partial
#global variable
temp_val="Celsius" 
def store_temp(set_temp):
    global temp_val
    temp_val=set_temp
def call_convert(rlabel,inputn):
    temp=inputn.get()

    if temp_val=="Celsius":
        f=float((float(temp)*9/5)+32)
        rlabel.config(text='%.lf Farenheit'%f)
        messagebox.showinfo('Temperature Convertor','Succesfully converted to Fahrenheit',)
    if temp_val == 'Fahrenheit':
        c=float((float(temp)-32)*5/9)
        rlabel.config(text='%.lf Celsius'%c)
        messagebox.showinfo('Temperature Converotr','Successfully converted to Celsius')

root = tk.Tk()
root.title('The Temperature Convertor')
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(1,weight=1)
number=tk.StringVar()
var=tk.StringVar()
input_label=tk.Label(root,text='enter temperature')
input_entry=tk.Entry(root,textvariable=number)
input_label.grid(row=1)
input_entry.grid(row=1,column=1)
result_label=tk.Label(root)
result_label.grid(row=3, columnspan=4)
dropdownlist=["Celsius","Fahrenheit"]
drop_down=tk.OptionMenu(root,var,*dropdownlist,command=store_temp)

drop_down.grid(row=1,column=2)
call_convert=partial(call_convert,result_label,number)
result_button=tk.Button(root,text='convert',command=call_convert)
result_button.grid(row=2,columnspan=2)
root.mainloop()