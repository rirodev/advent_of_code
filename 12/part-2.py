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

def move(sx, sy):
    best_path = {}
    last_best_path = None

    best_path[sx,sy] = 0
    while best_path != last_best_path:
        last_best_path = dict(best_path)
        for x in range(n_cols):
            for y in range(n_rows):
                c = get(x, y)
                if (x, y) not in best_path: continue
                if x < n_cols - 1 and ord(get(x + 1, y)) - ord(c) <= 1 and ((x+1,y) not in best_path or best_path[x+1,y] > best_path[x,y]+1): best_path[x+1,y] = best_path[x, y] + 1
                if y < n_rows - 1 and ord(get(x, y + 1)) - ord(c) <= 1 and ((x,y+1) not in best_path or best_path[x,y+1] > best_path[x,y]+1): best_path[x,y+1] = best_path[x, y] + 1
                if x > 0 and ord(get(x - 1, y)) - ord(c) <= 1 and ((x-1,y) not in best_path or best_path[x-1,y] > best_path[x,y]+1): best_path[x-1,y] = best_path[x, y] + 1
                if y > 0 and ord(get(x, y - 1)) - ord(c) <= 1 and ((x,y-1) not in best_path or best_path[x,y-1] > best_path[x,y]+1): best_path[x,y-1] = best_path[x, y] + 1

    return best_path


shortest_a = None
count_a = 0
for x in range(n_cols):
    for y in range(n_rows):
        if get(x, y) == "a":
            best_path = move(x, y)
            if (E[0], E[1]) in best_path:
                dist = best_path[E[0], E[1]]
                count_a += 1
                print(count_a, "|", x, y, "got", dist)
                if shortest_a is None or dist < shortest_a:
                    shortest_a = dist
print(count_a)
print(shortest_a)
