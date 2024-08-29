# used to import the tkinter library and name it 'tk' for easier reference
import tkinter as tk
# used to import the colorchooser module from tkinter for color selection dialog
from tkinter import colorchooser
import random  # Import the random module for generating random positions

# SnakeGame class to represent the snake game
class SnakeGame:
    # Function used to initialize the game
    def __init__(self, master):
        # Set the master (main window) and configure its title and size
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("400x400")

        # Create a canvas to draw the game elements
        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=400)
        self.canvas.pack()

        # Sets default snake color, initial snake positions, direction, create food, and set initial game state
        self.snake_color = "green"  # Default snake color
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.food = self.create_food()
        self.paused = True  # Game starts paused
        self.update_scheduled = False  # Flag to track if an update is already scheduled

        # Binds the change_direction method to key events
        self.master.bind("<Key>", self.change_direction)

        # Creates the game menu and starts the game loop
        self.create_menu()
        self.update()

    # Function to restart the game
    def restart(self):
        # Destroys the current game window
        self.master.destroy()
        # Creates a new game window and runs it
        root = tk.Tk()
        game = SnakeGame(root)
        root.mainloop()

    # Function to create the game menu
    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        # used a restart to restart the game, change the snake color for customizability, and play/pause to start the game or pause to edit the snake color
        options_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Restart", command=self.restart)
        options_menu.add_command(label="Change Snake Color", command=self.change_snake_color)
        options_menu.add_command(label="Play/Pause", command=self.toggle_play_pause)

    # Function to toggle between play and pause states
    def toggle_play_pause(self):
        self.paused = not self.paused
        if not self.paused and not self.update_scheduled:
            self.update()

    # Function used to create the food on the canvas
    def create_food(self):
        x = random.randint(0, 39) * 10  # Random x position in the range [0, 390]
        y = random.randint(0, 39) * 10  # Random y position in the range [0, 390]
        # creates the circle food in the color red
        self.food_id = self.canvas.create_oval(x, y, x + 10, y + 10, fill="red")
        return x, y

    # Function to change the snake color using a color dialog
    def change_snake_color(self):
        color = colorchooser.askcolor()[1]
        # used to draw the snake color so you can see it on the canvas
        if color:
            self.snake_color = color
            self.draw()

    # Function used to change the snake direction based on key events
    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    # Function used to move the snake and update the game state based on the keypress direction
    def move(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= 10
        elif self.direction == "Down":
            y += 10
        elif self.direction == "Left":
            x -= 10
        elif self.direction == "Right":
            x += 10

        self.snake.insert(0, (x, y))

        # Checks to see if the snake has eaten the food
        if x == self.food[0] and y == self.food[1]:
            self.canvas.delete(self.food_id)
            self.food = self.create_food()
        else:
            self.snake.pop()

        # Checks for collisions and update the game accordingly. Will end the game if it detects a collision.
        self.check_collision()

        # If the game is not paused, schedule the next update. This function is used to actually pause all functions so the movement isn't scattered
        if not self.paused:
            self.update_scheduled = False
            self.master.after(100, self.update)
            self.update_scheduled = True

    # Function to check for collisions (wall or self) and handle game over
    def check_collision(self):
        x, y = self.snake[0]
        if x < 0 or x >= 400 or y < 0 or y >= 400 or (x, y) in self.snake[1:]:
            self.game_over()
        else:
            self.draw()

    # Function used to draw the snake on the canvas
    def draw(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, outline="white", fill=self.snake_color, tags="snake")

    # Function to display "Game Over" text on the canvas
    def game_over(self):
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Helvetica", 16), tags="game_over")

    # Function to update the game state
    def update(self):
        # If the game is not paused and "game_over" tag is not present, it will move the snake
        if not self.paused and "game_over" not in self.canvas.gettags("game_over"):
            self.move()

# Main entry point for the program
if __name__ == "__main__":
    # Creates the main window and starts the game
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()