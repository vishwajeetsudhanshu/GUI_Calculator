import tkinter as tk
def unit():
    # Conversion functions
    def convert_length(value, from_unit, to_unit):
        conversions = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1.0,
            'km': 1000.0,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }
        result = value * conversions[from_unit] / conversions[to_unit]
        return result

    def convert_mass(value, from_unit, to_unit):
        conversions = {
            'mg': 0.001,
            'g': 1.0,
            'kg': 1000.0,
            'lb': 453.592,
            'oz': 28.3495
        }
        result = value * conversions[from_unit] / conversions[to_unit]
        return result

    # GUI functions
    def convert():
        value = float(entry_value.get())
        from_unit = var_from.get()
        to_unit = var_to.get()
        conversion_type = var_type.get()

        if conversion_type == 'Length':
            result = convert_length(value, from_unit, to_unit)
            result_label.config(text=f"{result:.4f} {to_unit}")
        elif conversion_type == 'Mass':
            result = convert_mass(value, from_unit, to_unit)
            result_label.config(text=f"{result:.4f} {to_unit}")

    # Create the main window
    window = tk.Tk()
    window.title("Mathematical Unit Conversion")
    window.geometry("400x300")

    # Create conversion type selection
    var_type = tk.StringVar()
    var_type.set('Length')
    type_label = tk.Label(window, text="Conversion Type:")
    type_label.pack()
    type_menu = tk.OptionMenu(window, var_type, 'Length', 'Mass')
    type_menu.pack()

    # Create value entry
    value_label = tk.Label(window, text="Value:")
    value_label.pack()
    entry_value = tk.Entry(window)
    entry_value.pack()

    # Create "from" unit selection
    var_from = tk.StringVar()
    var_from.set('mm')
    from_label = tk.Label(window, text="From Unit:")
    from_label.pack()
    from_menu = tk.OptionMenu(window, var_from, 'mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi')
    from_menu.pack()

    # Create "to" unit selection
    var_to = tk.StringVar()
    var_to.set('mm')
    to_label = tk.Label(window, text="To Unit:")
    to_label.pack()
    to_menu = tk.OptionMenu(window, var_to, 'mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi')
    to_menu.pack()

    # Create conversion button
    convert_button = tk.Button(window, text="Convert", command=convert)
    convert_button.pack()

    # Create result label
    result_label = tk.Label(window, text="")
    result_label.pack()

    # Start the GUI
    window.mainloop()

