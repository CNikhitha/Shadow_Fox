AUSTRALIA = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
INDIA = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
city = input("Enter a city name: ").strip()
if city in AUSTRALIA:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in INDIA:
    print(f"{city} is in India")
else:
    print(f"Sorry, I don't know where {city} is.")
