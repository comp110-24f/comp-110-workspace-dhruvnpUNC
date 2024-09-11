"""Practice with conditionals"""


def less_than_10(num: int) -> None:
    """If number is less than 10"""
    if num < 10:
        print("Small Number!")
    elif num < 10 and num > 5:
        print("Medium Number!")
    else:
        print("Big Number!")
    print("Have a nice day!")


def should_i_eat(hungry: bool) -> None:
    """Tells me if I should eat based on hunger"""
    if hungry:
        print("eat food silly goose")  # then block
    else:
        print("Do your comp 110 hw instead")  # 'else block'
    print("I'm proud of you")  # either way be kind to yourself


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "Match"
    else:
        return "No Match"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
