import sys

class Monkey:

    instances = []

    @classmethod
    def info(cls):
        for m in cls.instances:
            print(f"Monkey {cls.instances.index(m)}:")
            print(f"  items: {','.join([str(v) for v in m.items])}")
            print(f"  op: {str(m.op_fn)}")
            print(f"  test_value: {m.test_value}")
            print(f"    a: {m.to_a}")
            print(f"    b: {m.to_b}")

    def __init__(self, items, op_fn, test_value, to_a, to_b):
        self.items = list(reversed(items))
        self.op_fn = op_fn
        self.test_value = test_value
        self.to_a = to_a
        self.to_b = to_b
        self.inspects = 0
        Monkey.instances.append(self)

    def add(self, item):
        self.items.insert(0, item)
    
    def op(self, item):
        return self.op_fn(item)

    def test(self, item):
        return item % self.test_value == 0

    def throw(self, item):
        if self.test(item):
            Monkey.instances[self.to_a].add(item)
        else:
            Monkey.instances[self.to_b].add(item)

    def turn(self, lcm):
        while len(self.items) > 0:
            self.inspects += 1
            item = self.items.pop()
            item = self.op(item)
            item = item % lcm
            self.throw(item)
    
    @classmethod
    def round(cls, lcm):
        for m in cls.instances:
            m.turn(lcm)

    @classmethod
    def show_items(cls):
        for i, m in enumerate(cls.instances):
            print(f"Monkey {i}: {', '.join([str(v) for v in m.items])}")

    @classmethod
    def lcm(cls):
        test_values = [m.test_value for m in cls.instances]
        d = max(test_values)
        while not all(d % v == 0 for v in test_values):
            d += 1
        return d

# Parsing
def parse():

    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
   
    line_ix = 0
    def get_line():
        nonlocal line_ix
        l = lines[line_ix] 
        line_ix += 1
        return l
   
    def op_fn_builder(op_str, value_str):
        def fn(old):
            value = old if value_str == "old" else int(value_str)
            return old * value if op_str == "*" else old + value
        return fn

    def get_items(): return [int(v) for v in get_line().split(":")[1].split(",")]
    def get_op_fn(): return op_fn_builder(*get_line().split("=")[1].split(" ")[2:4])
    def get_test_value(): return int(get_line().split("by")[1])
    def get_to_a(): return int(get_line().split("monkey")[1])
    def get_to_b(): return int(get_line().split("monkey")[1])
    
    while line_ix < len(lines):
        line_ix += 1 # skip header
        items = get_items()
        op_fn = get_op_fn()
        test_value = get_test_value()
        to_a = get_to_a()
        to_b = get_to_b()
        line_ix += 1 # skip blank line
        monkey = Monkey(items, op_fn, test_value, to_a, to_b)

parse()
lcm = Monkey.lcm()
for i in range(int(sys.argv[2])):
    Monkey.round(lcm)
    if i % 100 == 0:
        print(i)

    
ms = sorted(Monkey.instances, key=lambda m: m.inspects)
totals = [m.inspects for m in ms]
print(totals)
top_2, top_1 = totals[-2:]
print(top_2 * top_1)
