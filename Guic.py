
import tkinter as tk
from math import sin, cos, tan, sqrt, exp, log

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("IMTEYAZ ALAM Calculator")
        self.entry = tk.Entry(self.window, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
            'C', 'ce', 'x!', '%'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.window, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.window, text="sin", width=5, command=lambda: self.click_button('sin')).grid(row=5, column=0)
        tk.Button(self.window, text="cos", width=5, command=lambda: self.click_button('cos')).grid(row=5, column=1)
        tk.Button(self.window, text="tan", width=5, command=lambda: self.click_button('tan')).grid(row=5, column=2)
        tk.Button(self.window, text="sqrt", width=5, command=lambda: self.click_button('sqrt')).grid(row=5, column=3)
        tk.Button(self.window, text="exp", width=5, command=lambda: self.click_button('exp')).grid(row=6, column=0)
        tk.Button(self.window, text="log", width=5, command=lambda: self.click_button('log')).grid(row=6, column=1)
        tk.Button(self.window, text="(", width=5, command=lambda: self.click_button('(')).grid(row=6, column=2)
        tk.Button(self.window, text=")", width=5, command=lambda: self.click_button(')')).grid(row=6, column=3)
        
    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'sin':
            try:
                result = sin(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'cos':
            try:
                result = cos(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'tan':
            try:
                result = tan(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'sqrt':
            try:
                result = sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'exp':
            try:
                result = exp(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'log':
            try:
                result = log(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))

        

            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)


            

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()