"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730767591"


def input_word() -> str:
    """Prompts the user to input a word and checks to see if its 5 letters long."""
    typed_word: str = input("Enter a 5-character word: ") #prompts the user for input
    if len(typed_word) != 5: #checks to see if the length of a string is exactly 5 characters.
        print("Error: word must contain 5 characters.")
        exit()
    return typed_word


def input_letter() -> str:
    """Prompts a user to input a letter and checks to see if its exactly one character."""
    typed_letter = input("Enter a single character: ") #prompts the user for input
    if len(typed_letter) != 1: #checks to see if the length of the input is exactly one character.
        print("Error: Character must be a single character.")
        exit()
    return typed_letter


def contains_char(word: str, letter: str) -> None:
    """Checks to see how many instances of a letter appears in a given word."""
    char_count: int = 0 #counts how many times a letter appears in a given word
    print("Searching for " + letter + " in " + word)

    #checks every index of the word to find a matching character, and increases the char_count when a match is found.
    if word[0] == letter:
        char_count += 1
        print(letter + " found at index 0")
    if word[1] == letter:
        char_count += 1
        print(letter + " found at index 1")
    if word[2] == letter:
        char_count += 1
        print(letter + " found at index 2")
    if word[3] == letter:
        char_count += 1
        print(letter + " found at index 3")
    if word[4] == letter:
        char_count += 1
        print(letter + " found at index 4")

    #Checks to see how many instances of a letter is found and prints the corressponding output message.
    if char_count == 1:
        print(str(char_count) + " instance of " + letter + " found in " + word)
    elif char_count == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(char_count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Where the code will be ran."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
