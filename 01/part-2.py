# Read input
with open("input.txt") as f:
    lines = f.readlines()

# Clean
lines = [l.strip() for l in lines]

# Parse elf calorie lists
elf_cal_counts = []
curr_cals = 0
for ix, line in enumerate(lines):
    if line:
        v = int(line)
        curr_cals += v
    else:
        elf_cal_counts.append(curr_cals)
        curr_cals = 0

# Print result
print(sum(sorted(elf_cal_counts)[-3:]))

