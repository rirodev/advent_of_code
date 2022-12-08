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
total_visible = len(trees) * 2 + (len(trees[0]) - 2) * 2
for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1):
        
        def blocking(i2, j2):
            return trees[i2][j2] >= trees[i][j]

        vis_l = True
        vis_r = True
        vis_u = True
        vis_d = True

        i2 = i - 1
        while i2 >= 0:
            if blocking(i2, j):
                vis_l = False
                break
            i2 -= 1

        i2 = i + 1
        while i2 < len(trees):
            if blocking(i2, j):
                vis_r = False
                break
            i2 += 1

        j2 = j - 1
        while j2 >= 0:
            if blocking(i, j2):
                vis_u = False
                break
            j2 -= 1

        j2 = j + 1
        while j2 < len(trees[0]):
            if blocking(i, j2):
                vis_d = False
                break
            j2 += 1

        if vis_l or vis_r or vis_u or vis_d:
            total_visible += 1

log()
print(total_visible)
