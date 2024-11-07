"""A game where you have to guess the secret number!"""

__author__: str = "730767591"


def guess_a_number() -> None:
    """A function that helps us determine if a input is equal, greater, or less than the secret number"""
    secret: int = 7
    guess: str = input("Guess a number: ")
    print("Your guess was " + guess)

    if int(guess) == secret:
        print("You got it!")
    elif int(guess) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None

if __name__ == "__main__":
    """Where our code is ran."""
    guess_a_number()
