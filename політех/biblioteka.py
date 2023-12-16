from tkinter import *  
root = Tk() 
root.title('Шифр Частокола') 
e = (Entry(root, width=35, borderwidth=10)) 
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)  
root.geometry('400x200') 
title =Label(text='Введіть слово') 

#частокол
def code_1(): 
    input_srting = e.get() 
    output_string_1 = input_srting[::2] 
    output_string_2 = input_srting[1::2] 
    e.delete(0, END) 
    e.insert(0, output_string_2+output_string_1) 
     
#частокол через 3 
def code_2(): 
    input_srting = e.get() 
    output_string_1 = input_srting[::3] 
    output_string_2 = input_srting[1::3] 
    output_string_3 = input_srting[2::3] 
    e.delete(0, END) 
    e.insert(0, output_string_3+output_string_2+output_string_1) 
 
 
button_2 = Button(root, text='крок 2', command=code_1, fg="red", bg="blue", padx=25, pady=25) 
button_3 = Button(root, text='крок 3', command=code_2, fg="red", bg="blue", padx=25, pady=25) 
button_2.grid(row=1, column=0) 
button_3.grid(row=1, column=1) 
 
 
title.grid(row=0, column=0) 
 
root.mainloop()
 
