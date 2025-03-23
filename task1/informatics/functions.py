#a
arr = list(map(int, input().split()))

def find_min(arr:list):
    return min(arr)

print(find_min(arr))

#b
def power(a, n):
    return a ** n

a, n = map(float, input().split())

print(power(a, int(n)))

#c

def Xor(a, n):
    return a ^ n

x, y = map(int, input().split())

print(Xor(x, y))