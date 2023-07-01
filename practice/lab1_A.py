import math
x = 2
y = 6
z = 7
a =(math.sqrt(abs(x - 1)) - pow(abs(y), 1 / 3))/ (1 + pow(x, 2) / 2 + pow(z, 2) / 4)
b = x * pow((math.atan(z) + math.e), -(y + 3))
print(f"a = {a}")
print(f"b = {b}")