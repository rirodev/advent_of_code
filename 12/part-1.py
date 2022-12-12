import sys
sys.setrecursionlimit(10000)

with open(sys.argv[1], "r") as f:
    data = f.read().splitlines()

n_rows = len(data)
n_cols = len(data[0])
def get(x, y): return data[y][x]
def replace(a, b):
    for y in range(n_rows):
        data[y] = data[y].replace(a, b)

S = 0, 0
E = 0, 0
for y in range(n_rows):
    for x in range(n_cols):
        if get(x, y) == "S": S = x, y
        if get(x, y) == "E": E = x, y
replace("S", "a")
replace("E", "z")
for row in data: print(row)

best_path = {}

def move(x, y, steps):
    c = get(x, y)
    if (x, y) not in best_path:
        best_path[x, y] = steps
    elif steps < best_path[x, y]:
        best_path[x, y] = steps
    else:
        return
    if x > 0 and ord(get(x - 1, y)) - ord(c) <= 1: move(x - 1, y, steps + 1)
    if x < n_cols - 1 and ord(get(x + 1, y)) - ord(c) <= 1: move(x + 1, y, steps + 1)
    if y > 0 and ord(get(x, y - 1)) - ord(c) <= 1: move(x, y - 1, steps + 1)
    if y < n_rows - 1 and ord(get(x, y + 1)) - ord(c) <= 1: move(x, y + 1, steps + 1)
    

move(S[0], S[1], 0)
for y in range(n_rows):
    row_str = ""
    for x in range(n_cols):
        if (x, y) in best_path:
            row_str += " %02d " % best_path[x, y]
        else:
            row_str += " .. "
    print(row_str)
print(best_path[E[0], E[1]])
