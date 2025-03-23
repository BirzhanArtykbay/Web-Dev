#1
def make_bricks(small, big, goal):
    if big*5 == goal:
        return True
    elif big*5 > goal:
        return goal % 5 <= small
    else:
        max_big = min(goal//5, big)
        remaining_length = goal - max_big*5
        return remaining_length <= small

#2
def lone_sum(a, b, c):
    num_occurrences = {a: 0, b: 0, c: 0}
    for num in (a, b, c):
        num_occurrences[num] = num_occurrences[num] +  1
    unique_nums = [num for num in num_occurrences if num_occurrences[num] == 1]
    return sum(unique_nums)

print(lone_sum(2, 3, 2))


#3
def lucky_sum(a, b, c):
    nums = [a, b, c]
    if 13 in nums:
        return sum(nums[:nums.index(13)])
    else:
        return sum(nums)

#4
def no_teen_sum(a, b, c):
    nums = [a, b, c]
    for i in range(len(nums)):
        if nums[i] == 15 or nums[i] == 16:
            continue
        if 13 <= nums[i] <= 19:
            nums[i] = fix_teen(nums[i])
    return sum(nums)


def fix_teen(n):
    return 0

#5
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    if num % 10 >= 5:
        return (num // 10 + 1) * 10
    else:
        return (num // 10) * 10

#6
def close_far(a, b, c):
  if abs(b-a) <= 1:
    if abs(c-a) >= 2 and abs(c-b) >= 2:
      return True
  elif abs(c-a) <= 1:
    if abs(b-a) >= 2 and abs(b-c) >= 2:
      return True
  return False


#7
def make_chocolate(small, big, goal):
    big_bars_needed = goal // 5
    if big_bars_needed <= big:

        goal -= big_bars_needed * 5
    else:

        goal -= big * 5

    if goal <= small:
        return goal
    else:
        return -1