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
def log(head, tail, size):
    grid_str = ""
    for i in range(size, -1, -1):
        row_str = ""
        for j in range(size):
            if head[1] == i and head[0] == j:
                row_str += "H"
            elif tail[1] == i and tail[0] == j:
                row_str += "T"
            elif (j, i) in hashes:
                row_str += "#"
            else:
                row_str += "."
        grid_str += row_str + "\n"
    print("======")
    print("======")
    print(grid_str[:-1])


def run():
    head = (0, 0)
    tail = (0, 0)
    for move in moves:
        head = (head[0] + move[0], head[1] + move[1])

        # Handle cases for same row or col
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
        
        hashes[tail] = True
        #log(head, tail, 20)

run()
print(len(hashes))
