# Number Guessing Game

A Python number guessing game built as a portfolio project while learning core Python fundamentals — from a plain console script up through a full graphical interface. The program picks a random number between 1 and 100, and the player tries to guess it with unlimited attempts, guided by real-time feedback.

Two versions are included:
- **`guess_game.py`** — the original console version
- **`gui.py`** — a graphical version built with Tkinter/ttk, featuring a custom dark theme

## Features

- Random number generation (1–100)
- Unlimited guesses with real-time high/low feedback
- Attempt counter, shown live and at the end of each round
- Input validation:
  - Rejects non-numeric input without crashing
  - Rejects guesses outside the 1–100 range
- Replay support — start a new round instantly without restarting the program
- **Persistent best-score tracking** — your fewest-attempts record is saved to `best_score.txt` and reloaded automatically the next time you play
- **GUI version (`gui.py`) additionally includes:**
  - Custom dark-themed interface (`ttk` styling, purple accent color)
  - "Guess" and "New Game" buttons
  - Submit a guess by pressing Enter, not just clicking
  - Color-coded feedback (green for success, red for invalid/incorrect)
  - Live-updating best score display

## How to Run

**Requirements:** Python 3.10+ (no external libraries needed — uses only Python's standard library)

Console version:
```bash
python guess_game.py
```

GUI version:
```bash
python gui.py
```

## How It Works

**Console version (`guess_game.py`):**
- Uses `while True` with `break` to control the game loop, avoiding duplicated guess-checking logic
- Game logic lives in a `main()` function that accepts and returns the current best score, rather than relying on global state
- Reads/writes `best_score.txt` with proper error handling for missing or corrupted save data

**GUI version (`gui.py`):**
- Built around a `NumberGuessingGUI` class, which keeps the game's state (secret number, attempts, best score) bundled with the interface that displays it
- Uses Tkinter's `ttk` module for themed widgets and a custom dark color palette
- Widget text updates dynamically via `StringVar` and `.config()`, rather than the window being rebuilt each turn
- The best score file is located relative to the script's own directory, so it works correctly regardless of where the program is run from

## Project Status

Both the console and GUI versions are complete and fully playable. This project was built incrementally, one concept at a time, with a focus on understanding *why* each piece of code works — not just getting it working.

## What I Learned

- Control flow: `if`/`elif`/`else`, `while` loops, `break`/`continue`
- Functions, parameters, and `return` values (and why they're preferable to global variables)
- Exception handling with `try`/`except` for both bad user input and file errors
- Basic file I/O (reading/writing persistent data between program runs)
- Event-driven programming with Tkinter (widgets, `command` callbacks, dynamic text updates)
