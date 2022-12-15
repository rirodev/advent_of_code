import sys
import json

def compare(left, right, depth):

    print(f"{' ' * depth}- Compare {left} vs {right}")
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

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()
    
    pair_ix = 0
    line_ix = 0
    correct = []
    while line_ix < len(lines):

        # Grab the pair, skipping newline if present
        pair_ix += 1 
        left = json.loads(lines[line_ix]); line_ix += 1
        right = json.loads(lines[line_ix]); line_ix += 1

        if line_ix < len(lines):
            if not lines[line_ix].strip(): line_ix += 1
        
        # Run
        print(f"== Pair {pair_ix:02d} ==")
        res = compare(left, right, 0)
        if res:
           correct.append(pair_ix)
        print(f"-- result = {'correct' if res else 'incorrect'}")

print(correct)
print(sum(correct))

