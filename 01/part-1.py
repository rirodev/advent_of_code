# Read input
with open("input.txt") as f:
    lines = f.readlines()

# Clean
lines = [l.strip() for l in lines]

# Parse elf calorie lists
most_cals = 0
curr_cals = 0
for ix, line in enumerate(lines):
    if line:
        v = int(line)
        curr_cals += v
    else:
        if curr_cals > most_cals:
            most_cals = curr_cals
        curr_cals = 0

# Print result
print(most_cals)

