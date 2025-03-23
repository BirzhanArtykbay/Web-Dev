#1
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  else:
    return 40 <= cigars <= 60

#2
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  return 1

#3
def squirrel_play(temperature, is_summer):
    if is_summer:
        return temperature >= 60 and temperature <= 100
    else:
        return temperature >= 60 and temperature <= 90

#4
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2

#5
def sorta_sum(a, b):
  if 10 <= a+b <= 19:
    return 20
  else:
    return a+b

#6
def alarm_clock(day, vacation):
    if vacation:
        if day in [0, 6]:
            return "off"
        else:
            return "10:00"
    else:
        if day in [0, 6]:
            return "10:00"
        else:
            return "7:00"

#7
def love6(a, b):
  return (a == 6 or b == 6) and (a+b == 6 or abs(a-b) == 6)

#8
def in1to10(n, outside_mode):
  if outside_mode:
    if 1 <= n <= 10:
      return True
    else:
      return False
  else:
    return n in range(1, 11)

#9
def near_ten(num: int) -> bool:
    return num % 10 <= 2 or num % 10 >= 8
