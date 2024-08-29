import tkinter as tk  # Imports the tkinter module and alias it as tk for easier reference in the code
import random  # Imports the random module for generating random numbers
import os  # Imports the os module for interacting with the operating system

# Dictionary of possible words and their categories
word_categories = {  # Defines a dictionary containing categories as keys and lists of words as values
    "animals": ["elephant", "giraffe", "zebra", "penguin", "butterfly"],  # Animals category
    "fruits": ["banana", "pineapple", "strawberry", "watermelon"],  # Fruits category
    "electronics": ["computer", "television", "keyboard", "headphones"],  # Electronics category
    "nature": ["mountain", "sunflower", "rainbow", "fireworks"]  # Nature category
}

class HangmanGame:  # Defines a class for the Hangman game
    def __init__(self, root):  # Constructor method for initializing the game instance
        self.root = root  # Store the root window object
        self.root.title("Hangman Game")  # Sets the title of the root window

        self.canvas = tk.Canvas(root, width=1280, height=720)  # Creates a canvas widget for drawing graphics
        self.canvas.pack()  # Packs the canvas widget into the root window

        self.buttons = []  # Initializes an empty list to keep track of buttons
        self.restart_button = None  # Initializes a variable to store the restart button
        self.game_over = False  # Initializes a flag to track whether the game is over or not

        try:  # Attempts to execute the following code
            self.reset()  # Calls the reset method to initialize the game
        except Exception as e:  # If an exception occurs, catch it and store it in variable e
            print("Error during initialization:", e)  # Prints an error message

    def reset(self):
        self.game_over = False # Reset the game over flag
        # Chooses a random category and word from the word_categories dictionary
        category = random.choice(list(word_categories.keys())) # Randomly selects a category
        self.category = category # Stores the selected category
        self.word = random.choice(word_categories[category]).lower() # Randomly select a word from the chosen category
        self.guesses = [] # Initializes an empty list to store guessed letters
        self.remaining_attempts = 7 # Sets the number of remaining attempts
        self.display_word = ['_' if char.isalpha() else char for char in self.word] # Initializes the display word
        self.update_display() #updates the display

        self.canvas.delete("message")  # Deletes any existing message on the canvas
        self.canvas.delete("category")  # Deletes any existing category on the canvas
        self.canvas.create_text(640, 50, text="Welcome to Hangman! v1.0", font=("Helvetica", 20), tag="message", anchor="n")  # Displays welcome message
        self.canvas.create_text(640, 80, text="Category: {}".format(category.capitalize()), font=("Helvetica", 16), tag="category", anchor="n")  # Displays category

        button_frame = tk.Frame(self.root)  # Creates a frame widget to hold the buttons
        button_frame.place(relx=0.5, rely=0.7, anchor="center")  # Centers the button frame

        for btn in self.buttons:  # Deletes existing buttons if they exist
            btn.destroy()  # Destroys each button

        self.buttons.clear()  # Clears the list of buttons

        for i in range(26):  # Creates letter buttons
            letter = chr(97 + i)  # Converts ASCII code to character
            btn = tk.Button(button_frame, text=letter, command=lambda l=letter: self.guess(l))  # Creates a button with the letter as text
            btn.grid(row=i // 7, column=i % 7, sticky="nsew", padx=3, pady=3)  # Positions the button in a grid layout
            self.buttons.append(btn)  # Adds the button to the list of buttons

        if self.restart_button:  # Creates or update the restart button
            self.restart_button.destroy()  # Destroys the restart button if it already exists

        self.restart_button = tk.Button(self.root, text="Restart", command=self.reset)  # Creates a new restart button
        self.restart_button.place(relx=0.5, rely=0.9, anchor="center")  # Centers the restart button

        self.load_image()  # Loads and places the image

    def guess(self, letter):  # Method to handle the player's guess
        if not self.game_over and letter not in self.guesses:  # If the game is not over and the letter has not been guessed before
            self.guesses.append(letter)  # Adds the guessed letter to the list of guesses
            if letter in self.word:  # If the guessed letter is in the word
                for i, char in enumerate(self.word):  # Iterates over the characters in the word
                    if char == letter:  # If the character matches the guessed letter
                        self.display_word[i] = letter  # Updates the display word with the guessed letter
                if "_" not in self.display_word:  # If there are no more underscores in the display word
                    self.game_over = True  # Sets the game over flag to True
                    self.update_display("You win!")  # Displays a win message
            else:  # If the guessed letter is not in the word
                self.remaining_attempts -= 1  # Decrement the remaining attempts
                if self.remaining_attempts == 0:  # If there are no remaining attempts
                    self.game_over = True  # Sets the game over flag to True
                    self.update_display('You lose! The word was "{}"'.format(self.word))  # Displays a lose message
            self.update_display()  # Updates the display

    def update_display(self, message=None):  # Method to update the display
        if not self.game_over:  # If the game is not over
            self.canvas.delete("word")  # Deletes the existing display word on the canvas
            self.canvas.create_text(640, 200, text=" ".join(self.display_word), font=("Helvetica", 24), tag="word", anchor="n")  # Displays the display word on the canvas

            self.canvas.delete("attempts")  # Deletes the existing attempts text on the canvas
            self.canvas.create_text(640, 300, text="Attempts left: {}".format(self.remaining_attempts), font=("Helvetica", 16), tag="attempts", anchor="n")  # Displays the remaining attempts on the canvas

            self.canvas.delete("guessed")  # Deletes the existing guessed letters on the canvas
            self.canvas.create_text(640, 350, text="Guessed: {}".format(" ".join(self.guesses)), font=("Helvetica", 16), tag="guessed", anchor="n")  # Displays the guessed letters on the canvas

            # Centers the image horizontally and position it below the guessing lines
            image_x = 960  # Horizontal position
            image_y = 360  # Vertical position
            image_file = "hangman{}.png".format(7 - self.remaining_attempts)  # Determines the image file based on remaining attempts
            if os.path.isfile(image_file):  # If the image file exists
                try:  # Attempts to execute the following code
                    self.image = tk.PhotoImage(file=image_file)  # Load the image
                    self.canvas.create_image(image_x, image_y, image=self.image, tag="image")  # Displays the image on the canvas
                except tk.TclError as e:  # If a TclError occurs, catch it and store it in variable e
                    print("Error loading image:", e)  # Print an error message
            else:  # If the image file does not exist
                print("Image file not found:", image_file)  # Prints a message indicating that the image file was not found

            # Disables guessed letters
            for btn in self.buttons:  # Iterates over the buttons
                if btn.cget("text") in self.guesses:  # If the button's text is in the guessed letters
                    btn.config(state="disabled")  # Disables the button
        else:  # If the game is over
            # Displays the final state of the word, attempts left, and guessed letters
            self.canvas.delete("word")  
            self.canvas.create_text(640, 200, text=" ".join(self.display_word), font=("Helvetica", 24), tag="word", anchor="n")
            self.canvas.delete("attempts")
            self.canvas.create_text(640, 300, text="Attempts left: {}".format(self.remaining_attempts), font=("Helvetica", 16), tag="attempts", anchor="n")
            self.canvas.delete("guessed")
            self.canvas.create_text(640, 350, text="Guessed: {}".format(" ".join(self.guesses)), font=("Helvetica", 16), tag="guessed", anchor="n")

            # Centers the image horizontally and position it below the guessing lines
            image_x = 960  
            image_y = 360  
            image_file = "hangman{}.png".format(7 - self.remaining_attempts)  #updates image based on attempts
            if os.path.isfile(image_file):  
                try:  
                    self.image = tk.PhotoImage(file=image_file)  
                    self.canvas.create_image(image_x, image_y, image=self.image, tag="image")  #creates image
                except tk.TclError as e:  
                    print("Error loading image:", e)  #prints error loading image if there is a tclerror
            else:  
                print("Image file not found:", image_file)  

            # Disables guessed letters
            for btn in self.buttons:  
                if btn.cget("text") in self.guesses:  
                    btn.config(state="disabled")  

        if message:  # If there is a message to display
            self.canvas.delete("message")  # Deletes any existing message on the canvas
            self.canvas.create_text(640, 100, text=message, font=("Helvetica", 20), tag="message", anchor="n")  # Displays the message on the canvas

    def load_image(self):  # Method to load and display the image
        # Centers the image horizontally and position it below the guessing lines
        image_x = 960  # Horizontal position
        image_y = 360  # Vertical position
        image_file = "hangman{}.png".format(7 - self.remaining_attempts)  # Determines the image file based on remaining attempts
        if os.path.isfile(image_file):  # If the image file exists
            try:  # Attempts to execute the following code
                self.image = tk.PhotoImage(file=image_file)  # Loads the image
                self.canvas.create_image(image_x, image_y, image=self.image, tag="image")  # Displays the image on the canvas
            except tk.TclError as e:  # If a TclError occurs, catch it and store it in variable e
                print("Error loading image:", e)  # Print an error message
        else:  # If the image file does not exist
            print("Image file not found:", image_file)  # Prints a message indicating that the image file was not found

if __name__ == "__main__":  # If the script is executed as the main program
    root = tk.Tk()  # Creates a Tkinter root window
    game = HangmanGame(root)  # Creates an instance of the HangmanGame class
    root.mainloop()  # Runs the Tkinter event loop to display the GUI and handle user interactions