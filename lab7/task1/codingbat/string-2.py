#1
def double_char(str):
    result = ""
    for char in str:
        result += char * 2
    return result

#2
def count_hi(str):
  return str.count('hi')

#3
def cat_dog(str):
  return str.count('cat') == str.count('dog')

#4
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count

#5
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a.endswith(b) or b.endswith(a)

#6
def xyz_there(str):
    if str.startswith("xyz"):
        return True

    for i in range(1, len(str) - 2):
        if str[i - 1] != '.' and str[i:i + 3] == 'xyz':
            return True
    return False
