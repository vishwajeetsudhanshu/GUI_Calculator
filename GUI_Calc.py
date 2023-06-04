import tkinter as tk
from tkinter import ttk
import Basic_calculator as bcc
import Temp_conversion as tc
import Unit_conv as uc
import Special_calc as sc
# Create the main window
window = tk.Tk()
window.title("Calculator and Converter")
window.geometry("400x300")

# Load the background image
background_image = tk.PhotoImage(file=r"C:\Users\vkshu\Downloads\back.png")

# Create a label to display the background image
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the title
title_label = ttk.Label(window, text="Select an Option:")
title_label.pack(pady=10)

# Create a combobox to select the calculator/converter
combo_box = ttk.Combobox(window, values=["Basic Calculator", "Special Calculator", "Unit Conversion", "Temperature Conversion"])
combo_box.pack()

# Function to handle the selection from the combobox
def handle_selection():
    selected_option = combo_box.get()
    
    # Perform the respective action based on the selected option
    if selected_option == "Basic Calculator":
        open_basic_calculator()
    elif selected_option == "Special Calculator":
        open_special_calculator()
    elif selected_option == "Unit Conversion":
        open_unit_conversion()
    elif selected_option == "Temperature Conversion":
        open_temperature_conversion()

# Create a button to confirm the selection
confirm_button = ttk.Button(window, text="Select", command=handle_selection)
confirm_button.pack(pady=10)

def open_basic_calculator():
    bcc.call_calc()
    
def open_special_calculator():
    sc.special()
    
def open_unit_conversion():
    uc.unit()

def open_temperature_conversion():
     tc.call_temp()

#label
lb1 = tk.Label(window, text="This Calculator Is Created by Vishwajeet & Vasudev ",font=("Times New Roman",10,"italic"),fg="blue")
lb1.pack()

# Start the main event loop
window.mainloop()
