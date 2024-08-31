import tkinter as tk
from math import sin, cos, tan, log, sqrt

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("ALAM CALCULATOR")
        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        

        buttons = [
            ('7', lambda: self.click_button('7')),
            ('8', lambda: self.click_button('8')),
            ('9', lambda: self.click_button('9')),
            ('/', lambda: self.click_button('/')),
            ('4', lambda: self.click_button('4')),
            ('5', lambda: self.click_button('5')),
            ('6', lambda: self.click_button('6')),
            ('*', lambda: self.click_button('*')),
            ('1', lambda: self.click_button('1')),
            ('2', lambda: self.click_button('2')),
            ('3', lambda: self.click_button('3')),
            ('-', lambda: self.click_button('-')),
            ('0', lambda: self.click_button('0')),
            ('.', lambda: self.click_button('.')),
            ('sin', lambda: self.math_function('sin')),
            ('cos', lambda: self.math_function('cos')),
            ('tan', lambda: self.math_function('tan')),
            ('log', lambda: self.math_function('log')),
            ('sqrt', lambda: self.math_function('sqrt')),
            ('=', lambda: self.calculate()),
            ('+', lambda: self.click_button('+'))
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button[0], width=5, command=button[1]).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_button(self, button):
        self.entry.insert(tk.END, button)
    
        
    
    

    def math_function(self, func):
        try:
            num = float(self.entry.get())
            if func == 'sin':
                result = sin(num)
            elif func == 'cos':
                result = cos(num)
            elif func == 'tan':
                result = tan(num)
            elif func == 'log':
                result = log(num)
            elif func == 'sqrt':
                result = sqrt(num)
            
                
                
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def calculate(self):
        try:
            result = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
                 

root = tk.Tk()
calc = Calculator(root)
root.mainloop()

