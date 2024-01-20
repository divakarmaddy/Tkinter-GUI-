import tkinter as tk
import random

def play_game():
    user_score = 0
    computer_score = 0

    def update_score():
        user_score_label.config(text=f"Your Score: {user_score}")
        computer_score_label.config(text=f"Computer Score: {computer_score}")

    def user_choice(choice):
        nonlocal user_score, computer_score
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        user_label.config(text="Your Choice: " + choice)
        computer_label.config(text="Computer's Choice: " + computer_choice)

        if choice == computer_choice:
            result_label.config(text="It's a tie!")
        elif (choice == "Rock" and computer_choice == "Scissors") or (choice == "Paper" and computer_choice == "Rock") or (choice == "Scissors" and computer_choice == "Paper"):
            result_label.config(text="You win this round!")
            user_score += 1
        else:
            result_label.config(text="Computer wins this round!")
            computer_score += 1

        update_score()

    def reset_scores():
        nonlocal user_score, computer_score
        user_score = 0
        computer_score = 0
        update_score()


    root = tk.Tk()
    root.title("Rock, Paper, Scissors")

    user_label = tk.Label(root, text="Your Choice: ")
    computer_label = tk.Label(root, text="Computer's Choice: ")
    result_label = tk.Label(root, text="")
    user_score_label = tk.Label(root, text=f"Your Score: {user_score}")
    computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}")

    rock_button = tk.Button(root, text="Rock", command=lambda: user_choice("Rock"))
    paper_button = tk.Button(root, text="Paper", command=lambda: user_choice("Paper"))
    scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice("Scissors"))
    reset_button = tk.Button(root, text="Reset Scores", command=reset_scores)

    user_label.pack()
    computer_label.pack()
    result_label.pack()
    user_score_label.pack()
    computer_score_label.pack()

    rock_button.pack()
    paper_button.pack()
    scissors_button.pack()
    reset_button.pack()

    root.mainloop()

if __name__ == "__main__":
    play_game()
