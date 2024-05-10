#Hangman Game: Create a graphical version of the hangman game using Python's Tkinter library
import tkinter as tk 
import random 

def guess_letter():
    global lives_remaining
    global guessed_letters

    guess = guess_entry.get().lower()  # Get the guess from the entry widget and convert to lowercase
    guess_entry.delete(0, tk.END)      # Clear the entry widget after each guess

    if guess in guessed_letters:
        # If the letter has already been guessed, do nothing
        return

    guessed_letters.append(guess)  # Add the guess to the list of guessed letters

    if guess not in word:
        # If the guess is incorrect, decrement lives remaining and update hangman figure
        lives_remaining -= 1
        update_hangman_figure()
    else:
        # If the guess is correct, update canvas to reveal correctly guessed letters
        update_word_display()

    if lives_remaining == 0:
        # If no lives remaining, game over
        game_over("You lose :(")
    elif "_" not in word_display:
        # If no underscores remaining, player wins
        game_over(f"Congratulations! You guessed the word: {word}")

def update_hangman_figure():
    # Draw hangman figure based on remaining lives
    # Define the coordinates for drawing different parts of the hangman figure
    if lives_remaining == 5:
        # Draw head
        myCanvas.create_oval(90, 100, 130, 140, outline="blue", width=2)
    elif lives_remaining == 4:
        # Draw body
        myCanvas.create_line(110, 140, 110, 200, fill="blue", width=2)
    elif lives_remaining == 3:
        # Draw left arm
        myCanvas.create_line(110, 160, 90, 140, fill="blue", width=2)
    elif lives_remaining == 2:
        # Draw right arm
        myCanvas.create_line(110, 160, 130, 140, fill="blue", width=2)
    elif lives_remaining == 1:
        # Draw left leg
        myCanvas.create_line(110, 200, 90, 220, fill="blue", width=2)
    elif lives_remaining == 0:
        # Draw right leg
        myCanvas.create_line(110, 200, 130, 220, fill="blue", width=2)

def update_word_display():
    global word_display

    # Update word display to reveal correctly guessed letters
    for i, letter in enumerate(word):
        if letter in guessed_letters:
            # If the letter has been guessed, update corresponding letter space on canvas
            myCanvas.itemconfig(word_spaces[i], text=letter) 
            word_display[i] = letter
            

def game_over(message):
    # Display game outcome message
    game_outcome_label.config(text=message)
    # Disable guess entry widget
    guess_entry.config(state="disabled")

root = tk.Tk()
root.title("Hangman Game")

myCanvas = tk.Canvas(root, bg="white", height=300, width=300)
myCanvas.create_text(20, 280, anchor="w", font="Purisa", text="Hangman")

simple_words = ["wizard", "archer", "summer", "guitar", "hitler", "planet", "python", "spyder"]
word = random.choice(simple_words)
word_length = len(word)

letter_spacing = 20
x_start = 120
y = 280
word_spaces = []  # List to store references to the letter spaces on the canvas
word_display = ["_"] * word_length  # List to track the displayed letters of the word

for i in range(word_length):
    x = x_start + i * letter_spacing
    word_space = myCanvas.create_text(x, y, anchor="w", font="Purisa", text="_")
    word_spaces.append(word_space)

myCanvas.pack()

# Entry widget for player's guesses
guess_entry = tk.Entry(root)
guess_entry.pack()

# Button to submit guess
submit_button = tk.Button(root, text="Submit Guess", command=guess_letter)
submit_button.pack()

# Label to display game outcome
game_outcome_label = tk.Label(root, text="", fg="red")
game_outcome_label.pack()
 
# Global variables
lives_remaining = 6
guessed_letters = []

root.mainloop()  