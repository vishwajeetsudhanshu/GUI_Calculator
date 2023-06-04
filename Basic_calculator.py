from tkinter import *
def call_calc():
        def button_click(number):
                current = entry.get()
                entry.delete(0, END)
                entry.insert(END, str(current) + str(number))

        def button_clear():
            entry.delete(0, END)

        def button_equal():
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, END)
            entry.insert(END, result)

        # Create a window
        window =Tk()
        window.title("Basic Calculator")

        # Create an entry widget
        entry = Entry(window, width=35, borderwidth=5)
        entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Define buttons
        button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
        button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
        button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
        button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
        button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
        button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
        button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
        button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
        button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
        button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
        button_add = Button(window, text="+", padx=39, pady=20, command=lambda: button_click("+"))
        button_subtract = Button(window, text="-", padx=41, pady=20, command=lambda: button_click("-"))
        button_multiply = Button(window, text="*", padx=40, pady=20, command=lambda: button_click("*"))
        button_divide = Button(window, text="/", padx=41, pady=20, command=lambda: button_click("/"))
        button_equal = Button(window, text="=", padx=89, pady=20, command=button_equal)
        button_clear = Button(window, text="Clear", padx=79, pady=20, command=button_clear)

        # Display buttons on the screen
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)

        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)

        button_0.grid(row=4, column=0)
        button_clear.grid(row=4, column=1, columnspan=2)

        button_add.grid(row=5, column=0)
        button_equal.grid(row=5, column=1, columnspan=2)

        button_subtract.grid(row=6, column=0)
        button_multiply.grid(row=6, column=1)
        button_divide.grid(row=6, column=2)

        # Start the main event loop
        window.mainloop()

