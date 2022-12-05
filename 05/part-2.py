# Get the lines
with open("input.txt", "r") as f:
    lines = [l.replace("\n", "") for l in f.readlines()]

# Remeber line index
line_ix = 0

# Parse the stack map
n = len(lines[0]) // 4 + 1
cols = [[] for _ in range(n)]
while "[" in lines[line_ix]:
    line = f"{lines[line_ix]}   "
    for i in range(n):
        if line[i*4:i*4+4] == "    ":
            # cols[i].insert(0, "x")
            pass
        else:
            cols[i].insert(0, line[i*4+1])
    line_ix += 1

# Skip the column labels line
line_ix += 1 

# Skip the empty line
line_ix += 1

def log():
    print("-" * 40)
    for (ix, c) in enumerate(cols):
        print(f"{ix}: {'|'.join(c)}")
    print("-" * 40)

# Process moves
log()
while line_ix < len(lines):
    line = lines[line_ix]
    parts = line.split(" ")
    n = int(parts[1])
    i_from = int(parts[3]) - 1
    i_to = int(parts[5]) - 1
    moving = cols[i_from][-n:]
    cols[i_from] = cols[i_from][:-n]
    cols[i_to] += moving 
    line_ix += 1
log()
print("".join([c[-1] for c in cols]))
