import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Global expression variable
expression = ""

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate final expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    equation.set("")

# StringVar() to update the input field
equation = tk.StringVar()

# Create input field frame
input_frame = tk.Frame(root)
input_frame.pack(expand=True, fill="both")

input_field = tk.Entry(input_frame, textvariable=equation, font=('Arial', 24), bd=0, justify="right")
input_field.pack(expand=True, fill="both", ipadx=8, ipady=15)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both")

# Define button layout
buttons = [
    ('7', '#4CAF50'), ('8', '#4CAF50'), ('9', '#4CAF50'), ('/', '#FF5722'),
    ('4', '#4CAF50'), ('5', '#4CAF50'), ('6', '#4CAF50'), ('*', '#FF5722'),
    ('1', '#4CAF50'), ('2', '#4CAF50'), ('3', '#4CAF50'), ('-', '#FF5722'),
    ('C', '#FFEB3B'), ('0', '#4CAF50'), ('=', '#FFEB3B'), ('+', '#FF5722'),
]

# Create buttons dynamically
row = 0
col = 0

for (text, color) in buttons:
    button = tk.Button(
        button_frame,
        text=text,
        bg=color,
        fg="white",
        font=('Arial', 18),
        bd=0,
        relief='ridge',
        command=lambda txt=text: press(txt) if txt not in ['=', 'C'] else equalpress() if txt == '=' else clear()
    )
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make grid cells expand equally
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

# Run the main loop
root.mainloop()
