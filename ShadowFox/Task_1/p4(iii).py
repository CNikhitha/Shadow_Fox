AUSTRALIA = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
INDIA = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
def find_country(city):
    if city in AUSTRALIA:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in INDIA:
        return "India"
    else:
        return None
c1 = input("Enter the first city: ").strip()
c2 = input("Enter the second city: ").strip()
country1 = find_country(c1)
country2 = find_country(c2)
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list.")