#
# Columns
#  1: A = Rock, B = Paper, C = Scissors <- Shape
#  2: X = Lose, Y = Draw, Z = Win <- Action
#
# Round Score (sum)
# - shape (rock=1, paper=2, scissors=3)
# - outcome (lose=0, draw=3, win=6)
#
# Total Score
# - sum rounds
#

require = { "X": "lose", "Y": "draw", "Z": "win" }
shape_choice = {
    "A": { "draw": "A", "win": "B", "lose": "C" },
    "B": { "lose": "A", "draw": "B", "win": "C" },
    "C": { "win": "A", "lose": "B", "draw": "C" }
}
shape_score = { "A": 1, "B": 2, "C": 3 }
outcome_score = { "lose": 0, "draw": 3, "win": 6 }

with open("input.txt") as f:
    lines = f.readlines()
plan = [l.split() for l in lines]
total = 0
for (elf, action) in plan:
    ending = require[action]
    score = shape_score[shape_choice[elf][ending]] + outcome_score[ending]
    total += score
print(total)
