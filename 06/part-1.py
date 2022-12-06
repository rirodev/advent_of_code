with open("input.txt", "r") as f:
    buffer = f.read()

i = 4
curr_4 = buffer[i-4:i]
while len(set(curr_4)) != 4:
    i += 1
    curr_4 = buffer[i-4:i]
print(i)
