import tkinter as tk
def special():

    def calculate_fibonacci():
        n = int(fibonacci_entry.get())
        result = fibonacci(n)
        fibonacci_result.config(text=f"Fibonacci({n}) = {result}")


    def calculate_factorial():
        n = int(factorial_entry.get())
        result = factorial(n)
        factorial_result.config(text=f"{n}! = {result}")


    def calculate_ackermann():
        m = int(ackermann_m_entry.get())
        n = int(ackermann_n_entry.get())
        result = ackermann(m, n)
        ackermann_result.config(text=f"Ackermann({m}, {n}) = {result}")


    def check_palindrome():
        string = palindrome_entry.get()
        result = palindrome(string)
        palindrome_result.config(text=f"Palindrome: {result}")


    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)


    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    def ackermann(m, n):
        if m == 0:
            return n + 1
        elif n == 0:
            return ackermann(m - 1, 1)
        else:
            return ackermann(m - 1, ackermann(m, n - 1))


    def palindrome(string):
        string = string.lower().replace(" ", "")
        return string == string[::-1]


    # Create the main window
    window = tk.Tk()
    window.title("Math Functions")
    window.geometry("400x300")

    # Fibonacci section
    fibonacci_label = tk.Label(window, text="Fibonacci:")
    fibonacci_label.pack()

    fibonacci_entry = tk.Entry(window)
    fibonacci_entry.pack()

    fibonacci_button = tk.Button(window, text="Calculate", command=calculate_fibonacci)
    fibonacci_button.pack()

    fibonacci_result = tk.Label(window, text="")
    fibonacci_result.pack()

    # Factorial section
    factorial_label = tk.Label(window, text="Factorial:")
    factorial_label.pack()

    factorial_entry = tk.Entry(window)
    factorial_entry.pack()

    factorial_button = tk.Button(window, text="Calculate", command=calculate_factorial)
    factorial_button.pack()

    factorial_result = tk.Label(window, text="")
    factorial_result.pack()

    # Ackermann section
    ackermann_label = tk.Label(window, text="Ackermann:")
    ackermann_label.pack()

    ackermann_m_entry = tk.Entry(window)
    ackermann_m_entry.pack()

    ackermann_n_entry = tk.Entry(window)
    ackermann_n_entry.pack()

    ackermann_button = tk.Button(window, text="Calculate", command=calculate_ackermann)
    ackermann_button.pack()

    ackermann_result = tk.Label(window, text="")
    ackermann_result.pack()

    # Palindrome section
    palindrome_label = tk.Label(window, text="Palindrome:")
    palindrome_label.pack()

    palindrome_entry = tk.Entry(window)
    palindrome_entry.pack()

    palindrome_button = tk.Button(window, text="Check", command=check_palindrome)
    palindrome_button.pack()

    palindrome_result = tk.Label(window, text="")
    palindrome_result.pack()

    # Start the application
    window.mainloop()
