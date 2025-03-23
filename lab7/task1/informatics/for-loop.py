#a
a = int(input())
b = int(input())

for i in range(a, b+1):
    if i%2==0:
        print(i, end=' ')

#b
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a,b+1):
    if i%d==c:
        print(i, end=" ")

#c
from math import sqrt

a = int(input())
b = int(input())

for i in range(a, b + 1):
    if int(sqrt(i)) ** 2 == i:
        print(i)
#d
x = input()
d = input()

print(x.count(d))

#e
x = input()
l = len(x)
x = int(x)

sum = 0

for i in range(l):
    sum += x % 10
    x = x//10

print(sum)
#f
x = input()

result = x[::-1]
while(result.startswith("0")):
    result = result.replace('0','',1)

print(result)
#g

x = int(input())

for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break

#h
x = int(input())

for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")

#i
import math

x = int(input())  # 16
cnt = 0 # 4
for i in range(1, int(math.sqrt(x))+1):  # 4
    if x % i == 0:
        cnt += 1
        if i != x // i:
            cnt += 1
print(math.sqrt(32))

#j
sum = 0

for i in range(100):
    x = int(input())
    sum += x

print(sum)

#k

N = int(input())
total = 0

for i in range(N):
    total += int(input())

print(total)

#l
decimal = int(input(), 2)
print(decimal)

#m

N = int(input())
cnt = 0

for i in range(N):
    num = input()
    if num == '0':
        cnt += 1

print(cnt)

