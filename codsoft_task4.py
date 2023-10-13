import tkinter as tk
import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


def user_choice_click(choice):
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Your choice: {choice}\nComputer's choice: {computer_choice}\n{result}")


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")


title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 16))
title_label.pack()

instruction_label = tk.Label(root, text="Choose your move:")
instruction_label.pack()


rock_button = tk.Button(root, text="Rock", command=lambda: user_choice_click("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: user_choice_click("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice_click("scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()


result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

root.mainloop()
