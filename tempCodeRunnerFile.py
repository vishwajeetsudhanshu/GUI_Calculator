# Load the background image
background_image = tk.PhotoImage(file=r"C:\Users\vkshu\Downloads\back.png")

# Create a label to display the background image
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
