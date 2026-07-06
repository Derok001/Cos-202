import tkinter as tk

# Create window
root = tk.Tk()
root.title("MATHEMATICAL CALCULATOR")
root.geometry("350x500")
root.resizable(False, False)

expression = ""

# Display
display = tk.Entry(root, font=("Arial", 22), bd=10, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


def press(key):
    global expression
    if key == "^":
        expression += "**"
        display.insert(tk.END, "^")
    else:
        expression += str(key)
        display.insert(tk.END, str(key))


def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def off():
    root.destroy()


buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('%',4,2), ('+',4,3),
    ('^',5,0), ('C',5,1), ('=',5,2), ('OFF',5,3)
]

for (text, row, col) in buttons:
    if text == "=":
        cmd = equal
    elif text == "C":
        cmd = clear
    elif text == "OFF":
        cmd = off
    else:
        cmd = lambda t=text: press(t)

    tk.Button(
        root,
        text=text,
        width=8,
        height=3,
        font=("Arial", 14),
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()