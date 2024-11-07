"""examples of dictionary syntax with Ice Cream Shop order Tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

print(len(ice_cream))  # prints 3
ice_cream["mint"] = 3  # add key-value entry to dictionary
print(ice_cream["chocolate"])  # prints 12
has_pbj: bool = "pbj" in ice_cream  # test if "pbj" key in icr-cream
ice_cream.pop("strawberry")  # remove item from dictionary
