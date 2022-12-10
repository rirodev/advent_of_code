import sys

with open(sys.argv[1], "r") as f:
    lines = [ l.strip() for l in f.readlines() ]

cycle = 0
value = 1
total = 0
X_values = []
def inc_cycle():
    global cycle, total
    cycle += 1
    X_values.append(value)


for line in lines:
    parts = line.split(" ")
    cmd = parts[0]
    args = parts[1:]
    if cmd == "noop":
        inc_cycle()
    elif cmd == "addx":
        inc_cycle()
        inc_cycle()
        value += int(args[0])


for x in X_values:
    print(x)

crt_i = 0
for r in range(6):
    row_str = ""
    for c in range(40):
        if c - 1 <= X_values[crt_i] <= c + 1:
            row_str += "#"
        else:
            row_str += "."
        crt_i += 1
    print(row_str)

