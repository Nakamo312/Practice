#1__________________________________
from random import randint, randrange

# генерация случайного четного и нечетных чисел
a = randint(1,2)*randint(1,50)
b = a+(randrange(1,50,2))
print('a =',a,'b =',b)
if a % 2:
    print('Нечетное число:',a)
else:
    print('Нечетное число:',b)

#2__________________________________
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

#поиск максимума
if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c
#поиск минимума
if a < b:
    if a < c:
        min = a
    else:
        min = c
else:
    if b < c:
        min = b
    else:
        min = c
#среднее
if a != max and a!= min:
    print('Среднее:',a)
elif b != max and b!= min:
    print('Среднее:',b)
else:
    print('Среднее:',c)

#3__________________________________
a = int(input('a = '))
b = int(input('b = '))
if a % b == 0:
    print('Число a делится нацело на число b ')
else:
    print('Остаток от деления:',a % b)
print('Частное:',a/b)

#4__________________________________

mem = float(input('Введите число:'))
answer = input('кб->б/б->кб (b/kb):')
if answer == 'b':
    print(mem*1024,"б")
elif answer == 'kb':
    print(mem/1024,"кб")
else:
    print('wrong answer')
#5__________________________________
char = int(input('Введите код символа ASCII:'))
if 65 < char < 90 or 97 < char < 122:
    print('Это код английской буквы')
else:
    print('Это иной символ')
print('Символ:',chr(char))

#6__________________________________
year = int(input('Введите год:'))
if year % 4 == 0:
    if year % 100:
        print('Этот год високосный')
    else:
        if year % 400:
            print('Этот год не високосный')
        else:
            print('Этот год високосный')
else:
    print('Этот год не високосный')

#7__________________________________

x = int(input('Координата x:'))
y = int(input('Координата y:'))

if x < 0:
    if y < 0:
        print('III четверть')
    else:
        print('II четверть')
else:
    if y < 0:
        print('IV четверть')
    else:
        print('I четверть')
#8__________________________________

x = float(input('x = '))
if x > 0:
    print(f'y ={2*x-10}')
elif x == 0:
    print(f'y = {0}')
else:
    print(f'y = {2 * abs(x) - 1}')
#9__________________________________
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

#поиск максимума
if a > b:
    if a > c:
        max = a
        summ = b + c
    else:
        max = c
        summ = b + a

else:
    if b > c:
        max = b
        summ = a + c
    else:
        max = c
        summ = b + a
if max < summ:
    if a == b == c:
        print('Равносторонний треугольник')
    elif (a == b) or (a == c) or (b == c):
        print('Равнобедренный треугольник')
    else:
        print('Разносторонний прямоугольник')
else:
    print('Такого треугольника не существует')
#10__________________________________
a = input('Введите число:')
max = 0
for i in a:
    if int(i) > max:
        max = int(i)
print('Наибольшая цифра:', max)
#11__________________________________

a = input('Введите число:')
summ = 0
mul = 1
for i in a:
    summ += int(i)
    mul *= int(i)
print('Произведение:', mul)
print('Сумма:', summ)
#12__________________________________
a = input('Введите число:')
count1 = 0
count2 = 0
for i in a:
    if int(i) % 2:
        count1 += 1
    else:
        count2 += 1
print('Количество нечетных:', count1)
print('Количество четных:', count2)
#13__________________________________
a = input('Введите число:')
b = ''
for i in range(len(a)-1,-1,-1):
    b += a[i]
print('Обратное число:',b)
#14__________________________________
summ = 0
for i in range(5):
    summ += int(input('Введите число:'))
print('Сумма чисел:',summ)

#15__________________________________
y = 0
for i in range(1,4):
    y += i + 5
print('y =',y)
#16__________________________________
c = int(input('c = '))
y = 0
for i in range(4):
    for j in range(6):
        y += i + 5
print('y =',y)