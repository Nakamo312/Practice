import math
x = 5
y = 1
z = 4
a =(3 + pow(math.e, y - 1)) / (1 + x * (y - math.tan(z)))
b = 1 + abs(y - x) + pow(y - x, 2) / 2 + pow(abs(y - z), 3) / 3
print(f"a = {a}")
print(f"b = {b}")