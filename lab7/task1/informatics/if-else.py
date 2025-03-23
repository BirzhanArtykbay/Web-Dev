#max
a = int(input())
b = int(input())

if a>b:
    print(a)
else:
    print(b)

#visokosnyi

c = int(input())

if (c % 4 == 0 and c % 100 != 0 ) or (c % 400 == 0):
    print("YES")
else:
    print("NO")

#testing system
res = int(input())
ans = int(input())

if res != 1 and ans != 1 and res == ans:
    print('YES')
else:
    print('NO')

#sign
x = int(input())

if x>0:
    print ('1')
elif x<0:
    print ('-1')
else:
    print('0')

#which is bigger
n = int(input())
k = int(input())

if n>k:
    print('1')
elif n<k:
    print('2')
else:
    print('0')