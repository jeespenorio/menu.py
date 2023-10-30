import tkinter as tk

# Function to handle the "New" menu item
def new_file():
    # Add your code to create a new file here
    pass

# Function to handle the "Open" menu item
def open_file():
    # Add your code to open a file here
    pass

# Function to handle the "Save" menu item
def save_file():
    # Add your code to save the file here
    pass

# Create a tkinter window
root = tk.Tk()
root.title("Menu File")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu items to the "File" menu
file_menu.add_command(label="New Import", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Main application loop
root.mainloop()
