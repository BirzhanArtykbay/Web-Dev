#1
def left2(str):
  return str[2:] + str[:2]

#2
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False

#3
def make_pi():
  pi = [3, 1, 4]
  return pi

#4
def common_end(a, b):
  if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    return True
  return False

#5
def sum3(nums):
  return sum(nums)

#6
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

#7
def reverse3(nums):
  return nums[::-1]

#8
def max_end3(nums):
  max_num = max(nums[0], nums[-1])
  return [max_num] * 3

#9
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) < 2:
    return sum(nums)
  else:
    return nums[0] + nums[1]

#10
def middle_way(a, b):
  return [a[1], b[1]]

#11
def make_ends(nums):
  return [nums[0], nums[-1]]

#12
def has23(nums):
  return 2 in nums or 3 in nums