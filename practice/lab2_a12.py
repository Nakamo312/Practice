
c = int(input(' Число возможных направлений: '))
k = int(input('Число тактов циклов регулирования (2-4): '))
if k == 2:
    a = 0.9
elif k == 3:
    a = 0.85
elif k == 4:
    a = 0.8
b = int(input('число основных циклообразующих направлений, требующих выделения полного такта'))
P_reg = 0
q = 0
mij = 0
for i in range(c):
    N = int(input('интенсивность движения: '))
    for j in range(b):
        Mj = int(input('число полос по даному направлению:'))
        for k in range(Mj):
            mij += 15
        ans = input('тип движения (лп/пп/п):')
        if ans == 'п':
            betta = 1
        elif ans == 'пп':
            betta = 0.9
        elif ans == 'лп':
            betta = 0.7
        else:
            betta = 1
        q += N / betta * mij
    P_reg += a / q * N
print(f'Пропускная способность  регулируемого движения: {P_reg}')