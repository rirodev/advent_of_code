trees = {}

def log():
    for i in trees:
        row = " ".join(f"{trees[i][j]}" for j in trees[i])
        print(row)

# Parse trees as 2D dict
with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]
    for i, row in enumerate(lines):
        if not row: continue
        trees[i] = {}
        for j, height in enumerate(row):
            trees[i][j] = height

# Count visible
best_score = 0
for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1):
        
        def blocking(i2, j2):
            return trees[i2][j2] >= trees[i][j]

        score_l = 0
        score_r = 0
        score_u = 0
        score_d = 0

        i2 = i - 1
        while i2 >= 0:
            score_l += 1
            if blocking(i2, j):
                break
            i2 -= 1

        i2 = i + 1
        while i2 < len(trees):
            score_r += 1
            if blocking(i2, j):
                break
            i2 += 1

        j2 = j - 1
        while j2 >= 0:
            score_u += 1
            if blocking(i, j2):
                break
            j2 -= 1

        j2 = j + 1
        while j2 < len(trees[0]):
            score_d += 1
            if blocking(i, j2):
                break
            j2 += 1

        score = score_l * score_r * score_u * score_d
        if score > best_score:
            best_score = score

log()
print(best_score)
