import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operator.get()
        if op == '+':
            result.set(num1 + num2)
        elif op == '-':
            result.set(num1 - num2)
        elif op == '*':
            result.set(num1 * num2)
        elif op == '/':
            if num2 != 0:
                result.set(num1 / num2)
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                result.set("")
        else:
            messagebox.showerror("Error", "Invalid operator")
            result.set("")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        result.set("")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="First Number:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Operator (+, -, *, /):").grid(row=1, column=0)
operator = tk.StringVar(value='+')
operator_menu = tk.OptionMenu(root, operator, '+', '-', '*', '/')
operator_menu.grid(row=1, column=1)

tk.Label(root, text="Second Number:").grid(row=2, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=4, column=0)
tk.Entry(root, textvariable=result, state='readonly').grid(row=4, column
