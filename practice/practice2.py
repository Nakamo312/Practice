#1__________________________________
string = input('Введите слова через пробел:')
string =string.split(',')
print('Количество слов:',len(string))

#2__________________________________

strings = []
answer = input('Введите строку:')
while answer != '':
    strings.append(answer)
    answer = input('Введите строку:')
max_len = 0
numbers = []
for i in range(len(strings)):
    if len(strings[i]) > max_len:
        max_len = len(strings[i])
for i in range(len(strings)):
    if len(strings[i]) == max_len:
        numbers.append(i)
print('Список наибольших строк:', numbers)
#3__________________________________
import array
answer = input('Введите строку:')
nums = array.array('i')
num = ''

for i in range(len(answer)):
    if 48 <= ord(answer[i]) <= 57:
        num += answer[i]
        if i == len(answer) -1:
            nums.append(int(num))
    else:
        if (48 <= ord(answer[i-1]) <= 57) and i != 0:
            num = int(num)
            nums.append(num)
            num = ''
print(nums)
#4__________________________________
answer = input('Введите строку:')
answer = answer.split(' ')
max_word = ''
max_len = 0
for i in answer:
    if len(i) > max_len:
        max_len = len(i)
        max_word = i
print('Самое длинное слово:',max_word)

#5__________________________________
answer = input('Введите строку:')
answer = list(answer)

i = 0
while answer[i] == ' ':
    answer.remove(answer[i])
new_str = ''
for i in range(len(answer)):
    if answer[i] != ' ' or (answer[i] == ' ' and answer[i-1] != ' ' and i != 0):
        new_str += answer[i]
if answer[-1] == ' ':
    new_str = new_str[:-1]
print(new_str)
#6__________________________________
answer = input('Введите строку:')
answer = list(answer)
count = 1
new_str = answer[0]
for i in range(1,len(answer)):
    if  answer[i] != answer[i-1]:
        new_str += str(count)
        new_str += answer[i]
        count = 1
    else:
        count += 1
    if i == len(answer) -1:
        new_str +=str(count)

print(new_str)
#7__________________________________
answer = input('Введите строку:')
count = 0
for i in answer:
    if i == ':':
        count += 1
answer = answer.replace(":","%")
print(answer,"Количество замен:",count)

#8__________________________________
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = []
for i in a:
    if i < 5:
        c.append(i)
print('Числа меньше 5:',c)
#9__________________________________
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
            break
print("Общие элементы списков:",c)

#10__________________________________

elems = input('Введите эл-ты списка через пробел')

elems = elems.split(' ')

buf = elems[0]
elems[0] = elems[len(elems)-1]
elems[len(elems)-1] = buf
print(elems)
#11__________________________________
a = [3,7,9]
a = [i**2 for i in a]
print(a)
#12__________________________________
a = [3,18,90,20,20,1,1,0,20]
i = 0
while i != (len(a) -1):
    if a[i] == 20:
        a.pop(i)
    i += 1
print(a)
#13__________________________________

a = [0 if 0 < i < 99  else 1 for i in range(100)]
print(a)
#14__________________________________

a = [i for i in range(46) if i % 2 == 1]
print(a)