from tkinter import * 
from tkinter import filedialog
import random

# Creates the main application window
main = Tk()
main.title("Alexa Tell Me A Joke ") # Sets the window title
main.geometry("500x450") # Sets the window size
main["bg"]='#22263d' # Sets the background color

# Open the text file containing jokes 
# Each jokes in the file should be written in one line in the format
with open("randomJokes.txt")as file_handler: # Reads each line and splits it at the ? mark into the setup, punchline
     jokes = [line.strip().split("?") for line in file_handler if "?" in line ] # Only lines that contain ? will be included
     
current_joke = None # Stores the current joke being displayed 
showing_setup = True # Tracks whether we are showing the setup or the punchline

def tellJoke(): # Handles displaying jokes in 2 steps by showing the setup question and then when pressed again it shows the punchline
    global current_joke, showing_setup
    # Clear the text box before showing a new joke or punchline 
    txtarea.delete("1.0", "end")
    
    # If showing_setup is true or no joke is selected yet
    if showing_setup or current_joke is None:
        # Pick a random joke from the list
        current_joke = random.choice(jokes)
        # Display only the setup or the first part of the joke
        txtarea.insert(END, current_joke[0] + "?")
        # Next time the button is clicked, shows the punchline
        showing_setup = False
    else:
        # Display both the setup and punchline together
        txtarea.insert(END, current_joke[0] + "?\n\n" + current_joke[1])
        # Resets back to the setup mode for the next joke
        showing_setup = True

# Create a text area to display jokes
txtarea = Text(main, width=40, height=10)
txtarea.place(x=20, y=40, height=250, width=450)

# Centers the Joke button horizontally 
window_width = 500 
button_width = 200
x_pos = (window_width - button_width) // 2 # Calculates the center poistion

# The button to trigger the joke displays here
Button(
  main,
  text="Alexa Tell Me a Joke!",
  command=tellJoke, bg="#8690c2", fg="white", font=("Arial", 14, "bold")
  ).place(x=x_pos, y=320, height=55, width=button_width)

# The button to close the application
Button(
  main,
  text="Quit",
  command=main.destroy,# Exits the main window
  bg="#8690c2", fg="white", font=("Arial", 14, "bold")
  ).place(x=200, y=390, height=45, width=100)



main.mainloop() # Keeps the window running until closed
