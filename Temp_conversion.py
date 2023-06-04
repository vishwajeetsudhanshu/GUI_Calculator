import tkinter as tk
def call_temp():

    def celsius_to_fahrenheit():
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_result.config(text=f"{fahrenheit} °F")

    def fahrenheit_to_celsius():
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_result.config(text=f"{celsius} °C")

    def fahrenheit_to_kelvin():
        fahrenheit = float(fahrenheit_entry.get())
        kelvin = (fahrenheit + 459.67) * 5/9
        kelvin_result.config(text=f"{kelvin} K")

    def kelvin_to_fahrenheit():
        kelvin = float(kelvin_entry.get())
        fahrenheit = kelvin * 9/5 - 459.67
        fahrenheit_result.config(text=f"{fahrenheit} °F")

    def celsius_to_kelvin():
        celsius = float(celsius_entry.get())
        kelvin = celsius + 273.15
        kelvin_result.config(text=f"{kelvin} K")

    def kelvin_to_celsius():
        kelvin = float(kelvin_entry.get())
        celsius = kelvin - 273.15
        celsius_result.config(text=f"{celsius} °C")

    # Create the main window
    window = tk.Tk()
    window.title("Temperature Converter")
    window.geometry("400x500")

    # Celsius to Fahrenheit
    celsius_label = tk.Label(window, text="Celsius:")
    celsius_label.pack()
    celsius_entry = tk.Entry(window)
    celsius_entry.pack()
    celsius_to_fahrenheit_button = tk.Button(window, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
    celsius_to_fahrenheit_button.pack()
    fahrenheit_result = tk.Label(window, text="")
    fahrenheit_result.pack()

    # Fahrenheit to Celsius
    fahrenheit_label = tk.Label(window, text="Fahrenheit:")
    fahrenheit_label.pack()
    fahrenheit_entry = tk.Entry(window)
    fahrenheit_entry.pack()
    fahrenheit_to_celsius_button = tk.Button(window, text="Convert to Celsius", command=fahrenheit_to_celsius)
    fahrenheit_to_celsius_button.pack()
    celsius_result = tk.Label(window, text="")
    celsius_result.pack()

    # Fahrenheit to Kelvin
    fahrenheit_to_kelvin_button = tk.Button(window, text="Convert to Kelvin", command=fahrenheit_to_kelvin)
    fahrenheit_to_kelvin_button.pack()
    kelvin_result = tk.Label(window, text="")
    kelvin_result.pack()

    # Kelvin to Fahrenheit
    kelvin_label = tk.Label(window, text="Kelvin:")
    kelvin_label.pack()
    kelvin_entry = tk.Entry(window)
    kelvin_entry.pack()
    kelvin_to_fahrenheit_button = tk.Button(window, text="Convert to Fahrenheit", command=kelvin_to_fahrenheit)
    kelvin_to_fahrenheit_button.pack()
    fahrenheit_result = tk.Label(window, text="")
    fahrenheit_result.pack()

    # Celsius to Kelvin
    celsius_to_kelvin_button = tk.Button(window, text="Convert to Kelvin", command=celsius_to_kelvin)
    celsius_to_kelvin_button.pack()
    kelvin_result = tk.Label(window, text="")
    kelvin_result.pack()

    # Kelvin to Celsius
    kelvin_to_celsius_button = tk.Button(window, text="Convert to Celsius", command=kelvin_to_celsius)
    kelvin_to_celsius_button.pack()
    celsius_result = tk.Label(window, text="")
    celsius_result.pack()

    # Start the main loop
    window.mainloop()
