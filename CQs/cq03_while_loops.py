"""Practice using a while loop to iterate over a string!"""

__author__: str = "730767591"

def num_instances(phrase: str, search_char: str) -> int:
    """Counts how times a specific character appears in a string and returns the value."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index +=1
    return count

print(num_instances(phrase="HelloHeLloHEllo", search_char="e"))