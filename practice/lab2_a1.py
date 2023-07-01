import math
from array import array


#1______________________________
x = int(input("x = "))
if x < 1:
    y = 5 / (pow(x - 7, 5))
elif x < 2:
    y = x
elif x > 0:
    y = math.sin(x)
print(f"y = {y}")

#2______________________________
x = int(input("x = "))
y = 10 / x if x < 5 else 0
print(f"y = {y}")

#3______________________________

arr = array('i', [-1, 25, -5, -7, 10, -31, 11, 507, 31, -8])

new_arr = array('i')
for i in arr:
    if i < 0:
        new_arr.append(i)
print(f"new array = {new_arr}")

#4______________________________
price = 5
for i in range(5,35,5):
    print(f"Цена за {i} кг: {i * price}")
