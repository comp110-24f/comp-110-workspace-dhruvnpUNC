def get_weather_report() -> str:
    """Tells us the weather depending on user input"""
    weather = input("What is the weather?")
    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


print(get_weather_report())
