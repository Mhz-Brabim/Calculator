from tkinter import *
# project calculator
gui = Tk()
gui.title("Calculator")
gui.configure(bg="black")

def button_click(num):
    current = enter.get()
    if current == "0":
        current = ""
    enter.delete(0, END)
    enter.insert(0, str(current) + str(num))

def button_clear():
    enter.delete(0, END)

def button_add():
    first_num = enter.get()
    global f_num, math
    math = "addition"
    f_num = float(first_num)
    enter.delete(0, END)

def button_divide():
    first_num = enter.get()
    global f_num, math
    math = "divide"
    f_num = float(first_num)
    enter.delete(0, END)

def button_minus():
    first_num = enter.get()
    global f_num, math
    math = "subtract"
    f_num = float(first_num)
    enter.delete(0, END)

def button_percent():
    first_num = enter.get()
    global f_num, math
    math = "percent"
    f_num = float(first_num)
    enter.delete(0, END)

def button_absolute():
    current_text = enter.get()
    if current_text:
        try:
            current_value = float(current_text)
            new_value = -current_value
            enter.delete(0, END)
            enter.insert(0, str(new_value))
        except ValueError:
            pass 

def button_multiply():
    first_num = enter.get()
    global f_num, math
    math = "multiply"
    f_num = float(first_num)
    enter.delete(0, END)

def button_equal():
    second_num = enter.get()
    enter.delete(0, END)
    try:
        second_num = float(second_num)
        if math == "addition":
            enter.insert(0, f_num + second_num)
        elif math == "multiply":
            enter.insert(0, f_num * second_num)
        elif math == "divide":
            enter.insert(0, f_num / second_num)
        elif math == "percent":
            percentage = (f_num / 100) * second_num
            enter.insert(0, percentage)
        elif math == "subtract":
            enter.insert(0, f_num - second_num)
    except ValueError:
        enter.insert(0, "Error") 

enter = Entry(gui, width=50, borderwidth=3, fg="white", bg="black")
enter.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button definitions
button_ac = Button(gui, text="AC", fg="black", bg="gray", padx=25, pady=25, command=button_clear, anchor="w")
button_ab = Button(gui, text="+/-", fg="black", bg="gray", padx=25, pady=25, command=button_absolute)
button_per = Button(gui, text="%", fg="black", bg="gray", padx=25, pady=25, command=button_percent)
button_div = Button(gui, text="/", fg="white", bg="#f29500", padx=25, pady=25, command=button_divide)
button_mult = Button(gui, text="x", fg="white", bg="#f29500", padx=25, pady=25, command=button_multiply)
button_min = Button(gui, text="-", fg="white", bg="#f29500", padx=25, pady=25, command=button_minus)
button_plus = Button(gui, text="+", fg="white", bg="#f29500", padx=25, pady=25, command=button_add)
button_equal = Button(gui, text="=", fg="white", bg="#f29500", padx=25, pady=25, command=button_equal)

button1 = Button(gui, text="1", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(1))
button2 = Button(gui, text="2", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(2))
button3 = Button(gui, text="3", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(3))
button4 = Button(gui, text="4", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(4))
button5 = Button(gui, text="5", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(5))
button6 = Button(gui, text="6", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(6))
button7 = Button(gui, text="7", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(7))
button8 = Button(gui, text="8", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(8))
button9 = Button(gui, text="9", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(9))
button0 = Button(gui, text="0", width=15, padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click(0))
button_dot = Button(gui, text=".", padx=25, pady=25, fg="white", bg="#A9A9A9", command=lambda: button_click("."))

# Button grid layout
button_ac.grid(row=1, column=0)
button_ab.grid(row=1, column=1)
button_per.grid(row=1, column=2)
button_div.grid(row=1, column=3)
button_mult.grid(row=2, column=3)
button_min.grid(row=3, column=3)
button_plus.grid(row=4, column=3)
button_equal.grid(row=5, column=3)

button1.grid(row=4, column=0, columnspan=1, padx=10, pady=10)
button2.grid(row=4, column=1, columnspan=1, padx=10, pady=10)
button3.grid(row=4, column=2, columnspan=1, padx=10, pady=10)
button4.grid(row=3, column=0, columnspan=1, padx=10, pady=10)
button5.grid(row=3, column=1, columnspan=1, padx=10, pady=10)
button6.grid(row=3, column=2, columnspan=1, padx=10, pady=10)
button7.grid(row=2, column=0, columnspan=1, padx=10, pady=10)
button8.grid(row=2, column=1, columnspan=1, padx=10, pady=10)
button9.grid(row=2, column=2, columnspan=1, padx=10, pady=10)
button0.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
button_dot.grid(row=5, column=2, columnspan=1, padx=10, pady=10)

gui.mainloop()
