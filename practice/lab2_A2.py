import math

lo = 1.5
la = 4

N = int(input('число полос движения: '))
Pi = 0
for i in range(N):
    v = int(input(f'скорость потока на {i+1} полосе: '))
    S = lo * pow(math.e, v / 25.2) + la
    P = 1000 * v / S
    Pi += P
print(f'Пропускная способность улицы: {Pi}')



