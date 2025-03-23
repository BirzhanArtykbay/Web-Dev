#a
from math import sqrt

N = int(input())

for i in range(1, N + 1):
    if int(sqrt(i)) ** 2 == i:
        print(i)

#b
N = int(input())
i = 1

while i**2 <= N:
    print(i**2)
    i += 1

#c
N = int(input())

i = 1
while i <= N:
    print(i)
    i *= 2

#d
N = int(input())

pow = 1

while pow < N:
    pow *= 2

if pow == N:
    print("YES")
else:
    print("NO")

#e
N = int(input())

pow = 1 
index = 0

while pow < N:
    pow *= 2
    index += 1

print(index)