import random
rolls = 20
count_6 = 0
count_1 = 0
count_two_6s_in_row = 0
previous_roll = None
for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    if previous_roll == 6 and roll == 6:
        count_two_6s_in_row += 1
    previous_roll = roll
print("\n--- Statistics ---")
print("Times rolled 6:", count_6)
print("Times rolled 1:", count_1)
print("Times rolled two 6s in a row:", count_two_6s_in_row)