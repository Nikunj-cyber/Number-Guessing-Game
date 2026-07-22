import os
import random
import tkinter as tk
from tkinter import ttk


class NumberGuessingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("470x430")
        self.root.minsize(450, 400)
        self.root.configure(bg="#060816")
        self.root.resizable(False, False)

        self.best_score = self._load_best_score()
        self.secret_number = None
        self.attempts = 0
        self.game_over = False

        self._build_ui()
        self.reset_game()

    def _load_best_score(self):
        score_path = os.path.join(os.path.dirname(__file__), "best_score.txt")
        try:
            with open(score_path, "r", encoding="utf-8") as handle:
                return int(handle.read().strip())
        except (FileNotFoundError, ValueError):
            return None

    def _save_best_score(self):
        score_path = os.path.join(os.path.dirname(__file__), "best_score.txt")
        with open(score_path, "w", encoding="utf-8") as handle:
            handle.write(str(self.best_score))

    def _build_ui(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TFrame", background="#060816")
        style.configure("Card.TFrame", background="#0f172a")
        style.configure("Hero.TFrame", background="#111c33")
        style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), foreground="#f8fafc", background="#111c33")
        style.configure("Body.TLabel", font=("Segoe UI", 10), foreground="#dbeafe", background="#0f172a")
        style.configure("Success.TLabel", font=("Segoe UI", 10, "bold"), foreground="#34d399", background="#0f172a")
        style.configure("Error.TLabel", font=("Segoe UI", 10, "bold"), foreground="#f87171", background="#0f172a")
        style.configure("Accent.TButton", padding=(12, 9), font=("Segoe UI", 10, "bold"))
        style.map(
            "Accent.TButton",
            background=[("active", "#8b5cf6"), ("pressed", "#6d28d9")],
            foreground=[("active", "#ffffff"), ("pressed", "#ffffff")],
        )
        style.configure("Ghost.TButton", padding=(12, 9), font=("Segoe UI", 10))
        style.map(
            "Ghost.TButton",
            background=[("active", "#1e293b"), ("pressed", "#0f172a")],
            foreground=[("active", "#f8fafc"), ("pressed", "#f8fafc")],
        )

        style.configure("Accent.TButton", borderwidth=0)
        style.configure("Ghost.TButton", borderwidth=0)
        style.configure("TEntry", fieldbackground="#111c33", foreground="#f8fafc", bordercolor="#334155")
        style.map("TEntry", bordercolor=[("focus", "#8b5cf6")])

        wrapper = ttk.Frame(self.root, padding=22, style="TFrame")
        wrapper.pack(fill="both", expand=True)

        card = ttk.Frame(wrapper, padding=0, style="Card.TFrame")
        card.pack(fill="both", expand=True)

        hero = ttk.Frame(card, padding=(24, 18), style="Hero.TFrame")
        hero.pack(fill="x")

        title = ttk.Label(hero, text="🎯 Guess the Number", style="Title.TLabel")
        title.pack(anchor="center")

        content = ttk.Frame(card, padding=20, style="Card.TFrame")
        content.pack(fill="both", expand=True)

        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(content, textvariable=self.status_var, style="Body.TLabel", wraplength=340, justify="center")
        self.status_label.pack(pady=(0, 12))

        self.congrats_label = ttk.Label(content, text="", wraplength=340, justify="center")
        self.congrats_label.pack(pady=(0, 10))

        self.entry = ttk.Entry(content, justify="center", width=24)
        self.entry.pack(pady=8)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        actions = ttk.Frame(content, style="Card.TFrame")
        actions.pack(pady=(10, 12))

        self.guess_button = ttk.Button(actions, text="Guess", command=self.check_guess, style="Accent.TButton")
        self.guess_button.pack(side="left", padx=(0, 8))
        self.guess_button.configure(width=12)

        self.new_game_button = ttk.Button(actions, text="New Game", command=self.reset_game, style="Ghost.TButton")
        self.new_game_button.pack(side="left")
        self.new_game_button.configure(width=12)

        for button in (self.guess_button, self.new_game_button):
            button.configure(cursor="hand2")

        self.feedback_var = tk.StringVar(value="")
        self.feedback_label = ttk.Label(content, textvariable=self.feedback_var, style="Body.TLabel", wraplength=340, justify="center")
        self.feedback_label.pack(pady=(2, 8))

        self.score_var = tk.StringVar(value=f"Best score: {'—' if self.best_score is None else self.best_score}")
        self.score_label = ttk.Label(content, textvariable=self.score_var, style="Body.TLabel")
        self.score_label.pack(pady=(6, 0))

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.game_over = False
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.status_var.set("A fresh round is ready. Pick a number from 1 to 100.")
        self.feedback_var.set("Good luck!")
        self._set_feedback_style("Body.TLabel")
        self.congrats_label.config(text="")

    def _set_feedback_style(self, style_name):
        self.status_label.configure(style=style_name)
        self.feedback_label.configure(style=style_name)
        self.congrats_label.configure(style=style_name)

    def check_guess(self):
        if self.game_over:
            return

        raw_guess = self.entry.get().strip()

        try:
            guess = int(raw_guess)
        except ValueError:
            self.status_var.set("Please enter a valid whole number.")
            self.feedback_var.set("Try again.")
            self._set_feedback_style("Error.TLabel")
            return

        if not 1 <= guess <= 100:
            self.status_var.set("Choose a number between 1 and 100.")
            self.feedback_var.set("That value is out of range.")
            self._set_feedback_style("Error.TLabel")
            return

        self.attempts += 1

        if guess < self.secret_number:
            self.status_var.set("Too low. Try a higher number.")
            self.feedback_var.set(f"Attempt {self.attempts} used.")
            self._set_feedback_style("Error.TLabel")
        elif guess > self.secret_number:
            self.status_var.set("Too high. Try a lower number.")
            self.feedback_var.set(f"Attempt {self.attempts} used.")
            self._set_feedback_style("Error.TLabel")
        else:
            self.game_over = True
            self.status_var.set("You got it!")
            self.feedback_var.set(f"Correct! You solved it in {self.attempts} attempt(s).")
            self._set_feedback_style("Success.TLabel")
            self.congrats_label.config(text="🎉 Fantastic work! You cracked the code! 🎉")

            if self.best_score is None or self.attempts < self.best_score:
                self.best_score = self.attempts
                self._save_best_score()
                self.score_var.set(f"Best score: {self.best_score}")

        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    NumberGuessingGUI(root)
    root.mainloop()