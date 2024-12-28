from tkinter import Tk, Entry, Button, StringVar
import math

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('350x550')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('arial bold', 28), textvariable=self.equation).place(x=0, y=0)

        
        buttons = [
            ('1', 0, 50), ('2', 90, 50), ('3', 180, 50),
            ('4', 0, 125), ('5', 90, 125), ('6', 180, 125),
            ('7', 0, 200), ('8', 90, 200), ('9', 180, 200),
            ('0', 0, 275), ('(', 90, 275), (')', 180, 275),
            ('C', 90, 350), ('+', 270, 125), ('-', 270, 275),
            ('*', 270, 200), ('/', 270, 50), ('=', 180, 350),
            ('%', 0, 350),('x²', 270, 350),('√', 0, 425),('Delete', 90, 425),
            ('sin', 0, 425), ('cos', 90, 425), ('tan', 180, 425), 
            ('sin⁻¹', 0, 475), ('cos⁻¹', 90, 475), 
            ('tan⁻¹', 180, 475)
        ]

        for (text, x, y) in buttons:
            if text == '=':
                Button(width=11, height=4, text=text, relief='flat', bg='red', command=self.solve).place(x=x, y=y)
            elif text == 'C':
                Button(width=11, height=4, text=text, relief='flat', bg='green', command=self.clear).place(x=x, y=y)
            elif text == 'Delete':
                Button(width=11, height=4, text='Delete', relief='flat', bg='green', command=self.delete_last).place(x=x, y=y)
            elif text == 'x²':
                Button(width=11, height=4, text=text, relief='flat', bg='orange', command=self.square).place(x=x, y=y)
            elif text == '√':
                Button(width=11, height=4, text=text, relief='flat', bg='orange', command=self.square_root).place(x=x, y=y)
            elif text == 'sin':
                Button(width=11, height=4, text=text, relief='flat', bg='orange', command=lambda: self.trig_func('sin')).place(x=x, y=y)
            elif text == 'cos':
                Button(width=11, height=4, text=text, relief='flat', bg='orange', command=lambda: self.trig_func('cos')).place(x=x, y=y)
            elif text == 'tan':
                Button(width=11, height=4, text=text, relief='flat', bg='orange', command=lambda: self.trig_func('tan')).place(x=x, y=y)
            elif text == 'sin⁻¹':
                Button(width=11, height=4, text=text, relief='flat', bg='orange', command=lambda: self.trig_func('asin')).place(x=x, y=y)
            elif text == 'cos⁻¹':
                Button(width=11, height=4, text=text, relief='flat', bg='orange', command=lambda: self.trig_func('acos')).place(x=x, y=y)
            elif text == 'tan⁻¹':
                Button(width=11, height=4, text=text, relief='flat', bg='orange', command=lambda: self.trig_func('atan')).place(x=x, y=y)
            else:
                Button(width=11, height=4, text=text, relief='flat', bg='yellow',
                    command=lambda value=text: self.show(value)).place(x=x, y=y)

    def trig_func(self, func):
        try:
            if not self.entry_value:
                return
            angle = eval(self.entry_value)
            if func == 'sin':
                result = math.sin(math.radians(angle))
            elif func == 'cos':
                result = math.cos(math.radians(angle))
            elif func == 'tan':
                result = math.tan(math.radians(angle))
            elif func == 'asin':
                result = math.degrees(math.asin(angle))
            elif func == 'acos':
                result = math.degrees(math.acos(angle))
            elif func == 'atan':
                result = math.degrees(math.atan(angle))
            
            self.equation.set(result)
            self.entry_value = str(result)  # Store the result for further calculations
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''
        

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

        
    def square(self):
        try:
            if not self.entry_value:
                return
            result = eval(self.entry_value)
            self.equation.set(result ** 2)
            self.entry_value = str(result ** 2)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

    def square_root(self):
        try:
            if not self.entry_value:
                return
            result = eval(self.entry_value)
            self.equation.set(math.sqrt(result))
            self.entry_value = str(math.sqrt(result))
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

          
    def delete_last(self):
        if self.entry_value:  
            self.entry_value = self.entry_value[:-1]  # Remove the last character
            self.equation.set(self.entry_value) 

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

   

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)  
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
