#a
N = int(input())
arr = input().split()

for i in range(0, N, 2):
    print(arr[i])

#b
N = int(input())
arr = input().split()

for i in range(1, N, 2):
    print(arr[i], end=" ")

#c
N = int(input())
arr = input().split()

cnt = 0

for i in arr:
    if int(i) > 0:
        cnt += 1

print(cnt)

#d
N = int(input())
arr = input().split()

cnt = 0
prev = int(arr[0])

for i in range(1, N):
    if int(arr[i]) > prev:
        cnt += 1
    prev = int(arr[i])

print(cnt)

#e
N = int(input())
arr = input().split()

arr = ["+" if int(num) > 0 else "-" for num in arr]


def check():
    i = 1
    prev = arr[0]
    while (i < N):
        if arr[i] == prev:
            return "YES"
        prev = arr[i]
        i += 1
    return "NO"


print(check())

#f
n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        count += 1

print(count)

#g
n = int(input())
arr = list(map(int, input().split()))

arr = arr[::-1]

for elem in arr:
    print(elem, end=" ")
