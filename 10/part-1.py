import sys

with open(sys.argv[1], "r") as f:
    lines = [ l.strip() for l in f.readlines() ]

cycle = 0
value = 1
show_cycles = [20, 60, 100, 140, 180, 220]
total = 0
def inc_cycle():
    global cycle, total
    cycle += 1
    if cycle in show_cycles:
        signal_strength = cycle * value
        total += signal_strength
        print(cycle, signal_strength)


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

print(total)
