
class File:

    def __init__(self, name, size):
        self._size = size
        self.name = name

    def size(self):
        return self._size

    def log(self, indent):
        print(f"{' ' * indent} - {self.name} [file, {self.size()}]")

class Folder:

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.items = {} 

    def add(self, item):
        self.items[item.name] = item

    def size(self):
        total = 0
        for name, item in self.items.items():
            total += item.size()
        return total

    def log(self, indent):
        print(f"{' ' * indent} - {self.name} [dir, {self.size()}]")
        for name, item in self.items.items():
            item.log(indent + 4)

    def get_folders_below_size(self, threshold):
        dirs_below = []
        for name, item in self.items.items():
            if isinstance(item, Folder): 
                dirs_below += item.get_folders_below_size(threshold)
        if self.size() < threshold:
            dirs_below.append(self)
        return dirs_below 

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

root = Folder(None, "/")

curr_dir = None
line_ix = 0
while True:

    if line_ix == len(lines):
        break

    # Get next command 
    line = lines[line_ix]
    parts = line.split(" ")
    line_ix += 1

    # Exec command
    cmd = parts[1]

    if cmd == "cd":
        dest = parts[2]
        if dest == "..":
            # print("cd ..")
            curr_dir = curr_dir.parent
        elif dest == "/":
            # print("cd /")
            curr_dir = root
        else:
            # print("cd", dest)
            curr_dir = curr_dir.items[dest]

    elif cmd == "ls":
        while not lines[line_ix].startswith("$"):
            parts = lines[line_ix].split(" ")
            if parts[0] == "dir":
                name = parts[1]
                if name not in curr_dir.items:
                    new_dir = Folder(curr_dir, name)
                    curr_dir.add(new_dir)
            else:
                size = int(parts[0])
                name = parts[1]
                if name not in curr_dir.items:
                    new_file = File(name, size)
                    curr_dir.add(new_file)
            line_ix += 1

            if line_ix == len(lines):
                break

print(root.log(0))
dirs = root.get_folders_below_size(100000)
for d in dirs:
    print(d.name, d.size())
print(sum(d.size() for d in dirs))
