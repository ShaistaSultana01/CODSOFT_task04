import tkinter as tk
import random

# Game choices
choices = ['Rock', 'Paper', 'Scissors']

# Scores
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(choices)

    # Determine winner
    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        comp_score += 1

    # Update labels
    user_choice_label.config(text=f"You chose: {user_choice}")
    comp_choice_label.config(text=f"Computer chose: {comp_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")

# Reset the game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_choice_label.config(text="You chose: ")
    comp_choice_label.config(text="Computer chose: ")
    result_label.config(text="Let's Play!", fg="black")
    score_label.config(text="Score  You: 0 | Computer: 0")

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x350")
root.resizable(False, False)

# Labels
tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16)).pack(pady=10)
user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 12))
user_choice_label.pack()

comp_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
comp_choice_label.pack()

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

play_again_button = tk.Button(root, text="Play Again", command=reset_game, bg="black", fg="white")
play_again_button.pack(pady=10)

# Run the app
root.mainloop()

