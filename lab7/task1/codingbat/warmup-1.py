#1
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

#2
def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  else:
    return False

#3
def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return a + b

#4
def diff21(n):
  if n >= 21:
    return abs(n-21)*2
  else:
    return abs(21-n)

#5
def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False

#6
def makes10(a, b):
  if a == 10 or b == 10 or a + b == 10:
    return True
  return False

#7
def near_hundred(n):
  return ((abs(100-n) <= 10) or (abs(200-n) <= 10))


#8
def pos_neg(a: int, b: int, negative: bool) -> bool:
    if negative:
        return a < 0 and b < 0
    return (a < 0 < b) or (b < 0 < a)


print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))

#9
def not_string(str):
  if str.startswith("not"):
    return str
  else:
    return "not " + str

#10
def missing_char(str, n):
    return str.replace(str[n], '', 1)

#11
def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str) - 1]  # can be written as str[1:-1]

    # last + mid + first
    return str[len(str) - 1] + mid + str[0]

#12
def front3(str):
  if len(str) < 3:
    return str*3
  else:
    return str[0:3]*3

