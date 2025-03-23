#1
def hello_name(name):
  return "Hello " + name + "!"

#2
def make_abba(a, b):
  return a + b + b + a

#3
def make_tags(tag, word):
  return "<%s>%s</%s>" %(tag, word, tag)

#4
def make_out_word(out, word):
  return out[0:2] + word + out[2:4]

#5
def extra_end(str):
  index = len(str)-1 - 1
  return str[index:len(str)]*3

#6
def first_two(str):
    if len(str) == 0:
        return ""
    elif len(str) < 2:
        return str
    return str[0:2]

#7
def first_half(str):
  return str[:len(str)//2]

#8
def without_end(str):
  return str[1: len(str)-1]

#9
def combo_string(a, b):
  if len(a) > len(b):
    long = a
    short = b
  else:
    long = b
    short = a
  return short + long + short

#10
def non_start(a, b):
    return a[1:] + b[1:]

#11
def left2(str):
  return str[2:] + str[:2]