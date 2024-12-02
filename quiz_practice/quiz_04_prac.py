"""practicing for the fourth comp 110 quiz"""


class Course:
    """Models the idea of a UNC Course."""

    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        if self.level >= 400:
            if prereq in self.prerequisites:
                return True
        else:
            return False


def find_courses(input_list: list[Course], prerequisite: str) -> list[str]:
    temp_list: list[str] = []
    for i in input_list:
        if i.level > 400:
            if prerequisite in i.prerequisites:
                temp_list.append(i.name)
    return temp_list


class Car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self, make: str, model: str, year: int, color: str, mileage: float):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def update_milage(self, miles: float):
        self.mileage += miles

    def display_info(self) -> None:
        print(
            f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Mileage: {self.mileage}"
        )


def calculate_depreciation(car: Car, depreciation_rate: float) -> float:
    return car.mileage * depreciation_rate


class HotCoca:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(
        self, hasWhip: bool, flavor: str, marshamallowCount: int, sweetness: int
    ):
        self.has_whip = hasWhip
        self.flavor = flavor
        self.marshmallow_count = marshamallowCount
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int) -> None:
        self.marshmallow_count += mallows
        self.sweetness += mallows * 2

    def __str__(self):
        if self.has_whip:
            return f"A {self.flavor} coca with whip, {self.marshmallow_count}, marshmallows, and level {self.sweetness} sweetness."
        else:
            return f"A {self.flavor} coca without whip, {self.marshmallow_count}, marshmallows, and level {self.sweetness} sweetness."


def order_cost(input_list: list[HotCoca]) -> float:
    cost: float = 0.0
    for i in input_list:
        if i.has_whip:
            cost += 2.50
        else:
            cost += 2.00
    return cost


# my_order: HotCoca = HotCoca(False, "vanilla", 5, 2)
# my_order.has_whip = True
# my_order.mallow_adder(2)
# viktoryas_order: HotCoca = HotCoca(True, "peppermint", 10, 2)
# cost: float = order_cost([my_order, viktoryas_order])
# print(cost) $5.00
# print(my_order)


class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def __add__(self, added_minutes: int):
        return TimeSpent(self.name, self.purpose, self.minutes + added_minutes)

    def reset(self) -> int:
        minutes: int = self.minutes
        self.minutes = 0
        return minutes

    def __str__(self):
        return f"{self.name} has spent {self.minutes // 60} hours and {self.minutes % 60} on screen time."


def most_by_purpose(input_list: list[TimeSpent], activity: str) -> str:
    most: int = 0
    person: str = ""
    for i in input_list:
        if i.purpose == activity:
            if i.minutes > most:
                most = i.minutes
                person = i.name
    return person


def fizzbuzz(n: int) -> int:
    if n <= 0:
        return -1

    if n == 1:
        return 0
    elif n % 2 == 0:
        return n + fizzbuzz(n - 1)
    else:
        return fizzbuzz(n - 1)


print(fizzbuzz(n=5))
print(fizzbuzz(n=4))
