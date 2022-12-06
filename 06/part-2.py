with open("input.txt", "r") as f:
    buffer = f.read()

n = 14
i = n
curr_n = buffer[i-n:i]
while len(set(curr_n)) != n:
    i += 1
    curr_n = buffer[i-n:i]
print(i)
