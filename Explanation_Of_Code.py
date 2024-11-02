import tkinter as tk  # Importing the tkinter library for creating GUI applications

# Initialize a global variable to store the current calculation string
calculation = ""

# Function to add a symbol (number/operator) to the calculation
def add_to_calculation(symbol):
    global calculation  # Use the global calculation variable
    calculation += str(symbol)  # Append the symbol to the calculation string
    text_result.delete(1.0, "end")  # Clear the text box
    text_result.insert(1.0, calculation)  # Insert the updated calculation string

# Function to evaluate the current calculation and display the result
def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))  # Evaluate the calculation string safely
        calculation = result  # Store the result as the new calculation
        text_result.delete(1.0, "end")  # Clear the text box
        text_result.insert(1.0, result)  # Display the result
    except:
        clear_field()  # Clear the field if there's an error
        text_result.insert(1.0, "ERROR")  # Show "ERROR" if evaluation fails

# Function to clear the calculation field
def clear_field():
    global calculation
    calculation = ""  # Reset the calculation string
    text_result.delete(1.0, "end")  # Clear the text box

# Function to handle keyboard inputs for the calculator
def key_press(event):
    key = event.keysym  # Capture the key pressed
    if key in '0123456789':  # Check if the key is a digit
        add_to_calculation(key)  # Add the digit to the calculation
    elif key in ('plus', 'minus', 'asterisk', 'slash'):  # Check for operator keys
        operator = {'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/'}
        add_to_calculation(operator[key])  # Map the key to the correct operator
    elif key == 'Return':  # Enter key for evaluation
        evaluate_calculation()
    elif key == 'BackSpace':  # Clear field with BackSpace key
        clear_field()
    elif key == 'parenleft':  # Left parenthesis key
        add_to_calculation('(')
    elif key == 'parenright':  # Right parenthesis key
        add_to_calculation(')')

# Create the main application window
root = tk.Tk()
root.title("Vikesh")# To give the title
root.geometry("300x275")  # Set window size
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))  # Create a text box for display
text_result.grid(columnspan=5)  # Place the text box across 5 columns

# Bind the key press event to the key_press function
root.bind("<Key>", key_press)

# Create buttons for digits, operators, and other functionalities, and place them in a grid layout
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial"))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial"))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial"))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial"))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial"))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial"))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial"))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial"))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial"))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial"))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial"))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial"))
btn_minus.grid(row=3, column=4)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial"))
btn_mul.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial"))
btn_div.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial"))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial"))
btn_close.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial"))
btn_clear.grid(row=6, column=1, columnspan=2)

btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial"))
btn_equal.grid(row=6, column=3, columnspan=2)

# Run the main event loop
root.mainloop()
