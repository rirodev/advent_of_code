import sys
import json

def compare(left, right, depth):
    
    # Both ints
    if type(left) == int and type(right) == int:
        if left < right: return True
        elif right < left: return False
        else: return None
    
    # Both lists
    if type(left) == list and type(right) == list:
        i = 0
        while True:
            left_out = i > len(left) - 1
            right_out = i > len(right) - 1
            if left_out and not right_out: return True
            if right_out and not left_out: return False
            if left_out and right_out: return None
            res = compare(left[i], right[i], depth + 2)
            if res is False: return False
            if res is True: return True
            i += 1
    
    # List (left) vs solo-int (right)
    if type(left) == list and type(right) == int:
        return compare(left, [right], depth + 2)
    
    # Solo-int (left) vs list (right)
    if type(left) == int and type(right) == list:
        return compare([left], right, depth + 2)

    raise NotImplementedError(f"Unsure what to do?\nLeft:{left}\nRight:{right}")

def log(packets):
    print(" == Packets == ")
    for p in packets:
        print(p)

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()
    lines.append("[[2]]")
    lines.append("[[6]]")
    packets = [ json.loads(l) for l in lines if l.strip() ]
    
    log(packets) 
    for i in range(len(packets) - 1):
        j = i
        while j >= 0:
            left = packets[j]
            right = packets[j + 1]
            if not compare(left, right, 0):
                packets[j] = right
                packets[j + 1] = left
                print(f"flipped {j}-{j+1}")
            else:
                print(f"correct {j}-{j+1}")
                break
            j -= 1
        log(packets) 
    
    found_2 = packets.index([[2]]) + 1
    found_6 = packets.index([[6]]) + 1
    print(found_2 * found_6)
