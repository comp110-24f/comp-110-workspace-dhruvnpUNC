"""A program that helps us plan a cozy tea party with our COMP110 friends!"""

__author__: str = "730767591"


def tea_bags(people: int) -> int:
    """Tells us how many tea bags to buy based on the amount of people attending."""
    return people * 2


def treats(people: int) -> int:
    """Tells us how many treats we need to buy based on the amount of people."""
    #Had issue with the function not returning properly until I realized in the return statement of the function I need to cast back the output from tea_bags * 1.5 as a int
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Helps us figure out the cost of our tea party."""
    return tea_count * 0.50 + treat_count * 0.75


def main_planner(guests: int) -> None:
    """Tells us how many treats and teabags to order, as well as the cost of the party."""
    print("A Cozy Tea Party for " + str(guests) + " People!") # Didn't know that python doesn't allow you to concatenate integer variables with strings.
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))))

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
