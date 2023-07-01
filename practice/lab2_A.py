from array import array

x = int(input("x = "))
#1______________________________
if x > 0:
    y = pow(x, 2) - 5
else:
    y = pow(x, 3) / 12
print(f"y = {y}")

#2______________________________
x = int(input("x = "))
y = 7 * x if x > 0 else 5
print(f"y = {y}")

#3______________________________

arr = array('i', [273, 5, 4, 3, 275, 31, 25, 8, 305])

new_arr = array('i')
for i in arr:
    if not(i % 2):
        new_arr.append(i)
print(f"new array = {new_arr}")

#4______________________________

string = input('Введите поизвольную строку: ')
flag = True
for i in range(len(string)):
    if not((i + 1) % 3):
        if not(string[i] == '/'):
            flag = False
print(f"Результат: {flag}")

