with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

az = "abcdefghijklmnopqrstuvwxyz"
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def ord(x):
    return az.index(x) + 1 if x.islower() else AZ.index(x) + 27

total = 0
for line in lines:
    i = len(line) // 2
    x = list( set(line[:i]) & set(line[i:]) )[0]
    total += ord(x)
print(total)

