"""Dictionary Utility Functions"""

__author__: str = "730767591"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverting a dictionary"""
    # creating the necessary lists to complete the tasks
    reversed_dict: dict[str, str] = {}
    input_keys: list[str] = []
    input_values: list[str] = []

    # creates a list that contains all the keys in the input dict
    for keys in input:
        input_keys.append(keys)

    # creates a list that contains all of the values in the input dict
    for values in input_keys:
        input_values.append(input[values])

    # checking to see if there are duplicate values in input dict
    for value_one in input_values:
        count = 0  # count variable is created to count duplicates
        for value_two in input_values:
            # The reason why we have two for loops is for comparison.
            # we want to take one index and compare it to every other
            # index to find duplicates
            # first for loop contains the index we want to compare
            # second for loop compares that index to every other index
            if value_one == value_two:
                count += 1

        if count > 1:
            # We check to see if count is greater than one
            # because the way we compared our list to find duplicates
            # means that the index we want to compare itself is counted as a duplicate
            # which it shouldn't be.
            # Therefore we check to see if there are two or more instead of one or more.
            raise KeyError("Duplicate values were found")
    # goes through the input_keys list we made earlier
    for item in input_keys:
        # uses the dict subscription notation to create new key-value pairs in temp_dict
        reversed_dict[input[item]] = item

    return reversed_dict  # returns the dict with the reversed values


def favorite_color(input: dict[str, str]) -> str:
    """Finding the favorite color in a given dict"""
    # creating all the variables needed to complete the task
    temp_dict: dict[str, int] = {}
    input_keys: list[str] = []
    input_values: list[str] = []
    temp_keys: list[str] = []
    color: str = ""
    highest: int = 0

    # creates a list with all of the input list keys
    for keys_input in input:
        input_keys.append(keys_input)

    # creates a list with all of the input list values
    for values_input in input_keys:
        input_values.append(input[values_input])

    # creates a new dict that will make counting the amount a value appears easier
    # by having a temp-dict that stores a key-value pair of the color
    # and the amount of times it appears
    # it becomes easier to see which color appeared the most
    for item in input_values:  # checks every value in the input_values list
        if item in temp_dict:
            # if the color exists in the dict, add an 1 to the corresponding value
            temp_dict[item] += 1
        else:
            # if the color doesn't exist in the dict, create a new key and set the
            # corresponding value to 1
            temp_dict[item] = 1

    # creates a list with all of the temp_dict keys
    for keys_temp in temp_dict:
        temp_keys.append(keys_temp)

    for j in temp_keys:  # checking to see which color occurs the most
        # due to how the dict is set up, accessing the value in the dict gives us an
        # int that tells us how many times that color appeared in the initial dict.
        if temp_dict[j] > highest:
            # after checking to see if the amount of times the color appears is
            # greater than the previously recorded highest value
            # we update the highest value
            # and set the color equal to the color that has appeared the most up until
            # this point
            highest = temp_dict[j]
            color = j

    return color


def count(input: list[str]) -> dict[str, int]:
    """counting how many times something appears in a dict"""
    temp_dict: dict[str, int] = {}
    for i in input:
        if i in temp_dict:
            temp_dict[i] += 1  # if it exists, add an 1 to the corresponding value
        else:
            # if it doesn't exist, create a new key and set the corresponding value to 1
            temp_dict[i] = 1

    return temp_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Categorizing words by first letter"""
    # creating variables needed to perform the task
    temp_dict: dict[str, list[str]] = {}
    temp_keys: list[str] = []

    # we traverse through the keys in the input list
    for i in input:
        # Goes through every element in the input list and looks at the first index
        # If the letter in the first index of the list isn't a key in temp_dict
        # A new key-value pair gets added with the first index of the list element
        # is the key and the value is an empty list
        # ex: {a: [], b: [], c: []}
        if i[0].lower() not in temp_dict:
            temp_dict[i[0].lower()] = []

    # creating a list of all of the keys in temp_dict
    # this makes adding the elements in the list to their corresponding
    # key-value pair in the dict easier
    for key in temp_dict:
        temp_keys.append(key)

    # what we do here is look through temp_keys list
    # this list contains all of the keys in temp_dict
    # Due to how we set up temp_dict earlier
    # all of the keys in temp_dict are single lowercase letters
    # which means temp_keys consists of single lowercase letters
    for j in temp_keys:
        # Since we need to add every element of the input list
        # to the corresponding key in temp_dict
        # we need to traverse all of the input list
        for k in range(len(input)):
            # first we check to see if the first index of the current list item in
            # its lowercase form is equal to the key value we stored in
            # the temp_keys list.

            # If it is we use subcription notation to access the corresponding
            # value in temp_dict using the current element of temp_keys to
            # access the value.

            # Since every value in temp_dict is a list, we need to append the element
            if j == input[k][0].lower():
                temp_dict[j].append(input[k])

    return temp_dict


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Updating the attendance of students"""
    if day not in input:
        # checking if a day of attendance is in the dict.
        # If it is not, then it creates a new key-value pair
        # The key is the day of attendance, and the value is an empty list
        input[day] = []
    if student not in input[day]:
        # adds the students name to the list containing the day of attendance.
        input[day].append(student)
    return None
