with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

dirs = {
  "R": (  1,  0 ),
  "L": ( -1,  0 ),
  "U": (  0,  1 ),
  "D": (  0, -1 ),
}
moves = []
for l in lines:
    d, n = l.split(" ")
    for i in range(int(n)):
        moves.append(dirs[d])

hashes = {}
def log(head, tails, size_x, size_y):
    grid_str = ""
    for i in range(size_x, -size_x, -1):
        row_str = ""
        for j in range(-size_y, size_y, 1):
            if head[1] == i and head[0] == j:
                row_str += "H "
            elif (j, i) in tails:
                row_str += str(tails.index((j, i)) + 1) + " "
            elif (j, i) in hashes:
                row_str += "# "
            else:
                row_str += ". "
        grid_str += row_str + "\n"
    print("======")
    print("======")
    print(grid_str[:-1])


def run():
    my_head = (0, 0)
    my_tails = []
    for i in range(9):
        my_tails.append((0, 0))
    
    log(my_head, my_tails, 50, 100)
    for move in moves:


        my_head = (my_head[0] + move[0], my_head[1] + move[1])

        knots = [my_head] + my_tails
        for i in range(len(my_tails)):
            head = my_head if i == 0 else my_tails[i-1]
            tail = my_tails[i]
            if head[0] == tail[0] or head[1] == tail[1]:
                if head[0] - tail[0] == 2: tail = (tail[0] + 1, tail[1])
                elif tail[0] - head[0] == 2: tail = (tail[0] - 1, tail[1])
                elif head[1] - tail[1] == 2: tail = (tail[0], tail[1] + 1)
                elif tail[1] - head[1] == 2: tail = (tail[0], tail[1] - 1)
            else:
                if abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1:
                    pass
                else:
                    if head[0] > tail[0]: tail = (tail[0] + 1, tail[1])
                    elif head[0] < tail[0]: tail = (tail[0] - 1, tail[1])
                    if head[1] > tail[1]: tail = (tail[0], tail[1] + 1)
                    elif head[1] < tail[1]: tail = (tail[0], tail[1] - 1)
            
            my_tails[i] = tail
        hashes[my_tails[-1]] = True
        #log(my_head, my_tails, 50, 100)

run()
print(len(hashes))
