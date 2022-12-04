groups = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    group = []
    for ix, line in enumerate(lines):
        group.append(line)
        if len(group) == 3:
            groups.append(group)
            group = []

az = "abcdefghijklmnopqrstuvwxyz"
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def ord(x):
    return az.index(x) + 1 if x.islower() else AZ.index(x) + 27

total = 0
for g in groups:
    total += ord(list(set(g[0]) & set(g[1]) & set(g[2]))[0])
print(total)

