"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730767591"


def input_word() -> str:
    """Prompts the user to input a word and checks to see if its 5 letters long."""
    typed_word: str = input("Enter a 5 letter word: ")
    if len(typed_word) != 5:
        print("Error: word must contain 5 characters.")
        exit()
    return typed_word


def input_letter() -> str:
    """Prompts a user to input a letter and checks to see if its exactly one character."""
    typed_letter = input("Enter a single character: ")
    if len(typed_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return typed_letter


def contains_char(word: str, letter: str) -> None:
    """Checks to see how many instances of a letter appears in a given word."""
    index: int = 0
    char_count: int = 0
    print("Searching for " + letter + " in " + word)
    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            char_count += 1
        index += 1

    if char_count > 0:
        print(str(char_count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    """Where the code will be ran."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
