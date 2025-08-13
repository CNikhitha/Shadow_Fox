justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Number of members:", len(justice_league))
justice_league.extend(["Batgirl", "Nightwing"])
print("After recruiting Batgirl & Nightwing:", justice_league)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman as leader:", justice_league)
justice_league.remove("Superman")  # remove original Superman position
flash = justice_league.index("Flash")
aquaman = justice_league.index("Aquaman")
if aquaman > flash:
    aquaman, flash = flash, aquaman
justice_league.insert(aquaman + 1, "Superman")
print("Superman between Aquaman & Flash:", justice_league)
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team assembled by Superman:", justice_league)
justice_league.sort()
print("Alphabetically sorted team:", justice_league)
print("New leader:", justice_league[0])