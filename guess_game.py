import random

def main(best_score):
    print("Welcome to the Guessing Game!")
    print("I have selected a secret number between 1 and 100.")
    print("Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            print(f"It took you {attempts} attempts.")

            if best_score is None or attempts < best_score:
                best_score = attempts
                with open("best_score.txt", "w") as file:
                    file.write(str(best_score))

            print(f"Your best score is: {best_score} attempts.")
            break

    return best_score


if __name__ == "__main__":
    try:
        with open("best_score.txt", "r") as file:
            best_score = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        best_score = None

    while True:
        best_score = main(best_score)
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break