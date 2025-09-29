import tkinter as tk
from math import sqrt

def handle_button_click(text):
    current = result_var.get()
    try:
        if text == "=":
            if current.strip():
                expression = current.replace("÷", "/").replace("×", "*")
                result = eval(expression)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                result_var.set(result)
        elif text == "%":
            import re
            match = re.search(r"(\d+\.?\d*)$", current)
            if match:
                number = float(match.group(1))
                new_number = str(number / 100)
                result_var.set(current[:match.start()] + new_number)
        elif text == "x²":
            if current and current.replace('.', '', 1).isdigit():
                result_var.set(str(float(current)**2))
        elif text == "√":
            if current and float(current) >= 0:
                result_var.set(str(sqrt(float(current))))
        else:
            result_var.set(current + text)
    except Exception:
        result_var.set("Error")

# Main window
root = tk.Tk()
root.title("Modern Calculator")
root.configure(bg="#1E1E2E")

# Display
result_var = tk.StringVar()
entry = tk.Entry(root, textvariable=result_var, font=("Helvetica", 28, "bold"),
                 justify="right", bg="#2E2E3E", fg="white", relief="flat", bd=10)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Buttons layout
buttons = [
    # Top advanced row
    ("x²",1,0),("√",1,1),("%",1,2),("÷",1,3),
    # Numbers 7-9 and ×
    ("7",2,0),("8",2,1),("9",2,2),("×",2,3),
    # Numbers 4-6 and -
    ("4",3,0),("5",3,1),("6",3,2),("-",3,3),
    # Numbers 1-3 and +
    ("1",4,0),("2",4,1),("3",4,2),("+",4,3),
    # Bottom row: 0, ., = (big horizontally)
    ("0",5,0),(".",5,1),("=",5,2,2)
]

# Button colors
colors = {
    "÷":"#FFA726","×":"#FFA726","-":"#FFA726","+":"#FFA726",
    "=":"#1ABC9C","x²":"#9B59B6","√":"#9B59B6","%":"#9B59B6"  # % in purple
}

# Create buttons
for b in buttons:
    text,row,col = b[:3]
    colspan = b[3] if len(b) >3 else 1
    btn = tk.Button(root, text=text, font=("Helvetica",14,"bold"),
                    bg=colors.get(text,"#616161"), fg="white",
                    activebackground="#333333", activeforeground="white",
                    relief="flat",
                    command=lambda t=text: handle_button_click(t))
    btn.grid(row=row,column=col,columnspan=colspan,sticky="nsew",padx=3,pady=3,ipadx=5,ipady=15)

# Grid weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Window size
root.geometry("480x680")
root.resizable(False,False)

# Keyboard bindings
root.bind("<Return>", lambda e: handle_button_click("="))
root.bind("<BackSpace>", lambda e: result_var.set(result_var.get()[:-1]))

root.mainloop()



