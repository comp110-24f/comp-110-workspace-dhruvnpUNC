"""Putting it all together to make wordle"""

__author__: str = "730767591"


def input_guess(secret_word: int) -> str:
    """Prompting the user to guess a word of a certain length"""
    guessing: bool = True #conditional for the while loop
    guess: str = input(f"Enter a {secret_word} character word: ")
    while guessing:
        if len(guess) == secret_word:
            guessing = False #when len of guess == secret_word guessing turns False exiting the while loop
        else:
            guess = input(f"That wasn't {secret_word} chars! Try again: ") #telling user to r   einput their guess
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1 #throws an error if char_guess is not equal to one
    isTrue: bool = False # tracking to see if an character is in a given word
    idx: int = 0 # counter for while loop
    while idx < len(secret_word):
        if char_guess == secret_word[idx]:
            isTrue = True #if a character is in the word, the variable turns true
        idx += 1
    return isTrue


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret) #throws an error if guess and secret aren't the same length
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojis: str = "" #empty string for the output of the emojis
    idx: int = 0 #counter for while loop
    while idx < len(secret):
        if secret[idx] == guess[idx]: #if the characters at both indexes match, add a green box
            emojis += GREEN_BOX 
        else:
            if contains_char(secret_word=secret, char_guess=guess[idx]): #if the letter is present in the word, add a yellow box
                emojis += YELLOW_BOX
            else: #if the letter is not present in the word, add a white box
                emojis += WHITE_BOX
        idx += 1
    return emojis


def main(secret: str) -> None:
    max_turns: int = 6 #max turns a players is granted
    current_turn: int = 1 #current turn count
    while current_turn <= max_turns:
        print(f"=== Turn {current_turn}/{max_turns} ===")
        guess = input_guess(secret_word=len(secret)) #uses input_guess function to prompt player for input
        print(emojified(guess=guess, secret=secret))
        if secret == guess: #checks to see if the user has guessed the secret word exactly
            print(f"You won in {current_turn}/{max_turns} turns!")
            break #exits out of the while loop once user guesses the word. Gave me a lot of trouble with grading because I used exit() initially ;-;
        current_turn += 1

    print(f"x/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
