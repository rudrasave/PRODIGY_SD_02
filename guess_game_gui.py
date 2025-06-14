import tkinter as tk
from tkinter import messagebox
import random

# --- Core Game Logic ---
class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.secret_number = None
        self.attempts = 0

        # Label
        self.label = tk.Label(root, text="Click Start to begin!", font=("Arial", 14))
        self.label.pack(pady=10)

        # Entry for guesses
        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        # Submit guess button
        self.submit_btn = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_btn.pack(pady=5)

        # Start game button
        self.start_btn = tk.Button(root, text="Start New Game", command=self.start_game)
        self.start_btn.pack(pady=5)

        # Feedback label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def start_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.label.config(text="Guess a number between 1 and 100")
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

    def check_guess(self):
        if self.secret_number is None:
            messagebox.showwarning("Start Game", "Please click 'Start New Game' first.")
            return

        guess = self.entry.get()
        if not guess.isdigit():
            self.result_label.config(text="⛔ Please enter a valid number!")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.secret_number:
            self.result_label.config(text="🔻 Too low! Try again.")
        elif guess > self.secret_number:
            self.result_label.config(text="🔺 Too high! Try again.")
        else:
            self.result_label.config(text=f"✅ Correct! Attempts: {self.attempts}")
            self.result_label.config(text=f"✅ You won in {self.attempts} attempts! 🎉")


# --- Run the App ---
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
