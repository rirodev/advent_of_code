#
# Columns
#  1: A = Rock, B = Paper, C = Scissors <- Elf
#  2: X = Rock, Y = Paper, Z = Scissors <- Me
#
# Round Score (sum)
# - shape (rock=1, paper=2, scissors=3)
# - outcome (lost=0, draw=3, won=6)
#
# Total Score
# - sum rounds
#

shape = { "X": 1, "Y": 2, "Z": 3 }
outcome = { "lose": 0, "draw": 3, "win": 6 }
result = {
    "A": { "X": outcome["draw"], "Y": outcome["win"], "Z": outcome["lose"] },
    "B": { "X": outcome["lose"], "Y": outcome["draw"], "Z": outcome["win"] },
    "C": { "X": outcome["win"], "Y": outcome["lose"], "Z": outcome["draw"] }
}

with open("input.txt") as f:
    lines = f.readlines()
plan = [l.split() for l in lines]
total = 0
for (elf, me) in plan:
    total += shape[me] + result[elf][me]
print(total)
