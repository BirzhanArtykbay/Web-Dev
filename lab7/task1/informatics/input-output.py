# gipotenusa
import math
a = int(input())
b = int(input())

c = math.sqrt(a*a + b*b)

print(c)

# next and previous
a = int(input())

print('The next number for the number %d is %d.' % (a, a + 1))
print('The previous number for the number %d is %d.' % (a, a - 1))

#apple-1
n = int(input())
k = int(input())

print(k//n)

#apple-2
print('Дележ яблок - 2' , k%n)

#mkad
v = int(input())
t = int(input())

if v>0:
    res = v*t
else:
    res = (-v*t)%109
    res = 109 - res

print(res%109)
