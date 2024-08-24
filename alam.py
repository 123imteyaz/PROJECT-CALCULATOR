import tkinter as tk
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GUI Calculator")
        
        self.entry = tk.Entry(self.window, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5)

        self.buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'pow',
            '1', '2', '3', '-', 'log',
            '0', '.', '=', '+', 'sin'
        ]

        row_val = 1
        col_val = 0

        for button in self.buttons:
            tk.Button(self.window, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

        tk.Button(self.window, text="cos", width=5, command=lambda: self.click_button('cos')).grid(row=2, column=4)
        tk.Button(self.window, text="tan", width=5, command=lambda: self.click_button('tan')).grid(row=3, column=4)

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'sqrt':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'pow':
            try:
                base = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "**")
                self.window.wait_variable(self.entry)
                result = math.pow(base, float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'log':
            try:
                result = math.log(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'sin':
            try:
                result = math.sin(math.radians(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'cos':
            try:
                result = math.cos(math.radians(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'tan':
            try:
                result = math.tan(math.radians(float(self.entry.get())))
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
