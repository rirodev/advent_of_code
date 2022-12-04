with open("input.txt", "r") as f:
    lines = f.readlines()

pairs = [l.strip().split(",") for l in lines]
count_contains = 0
for a, b in pairs:
    start_a, end_a = [ int(v) for v in a.split("-") ]
    start_b, end_b = [ int(v) for v in b.split("-") ]
    count_contains += (
        1
        if ( start_a <= start_b <= end_a and start_a <= end_b <= end_a )
        or ( start_b <= start_a <= end_b and start_b <= end_a <= end_b )
        else
        0
    )
print(count_contains)
