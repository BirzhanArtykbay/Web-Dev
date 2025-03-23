#1
def count_evens(nums: list) -> int:
    return sum(1 for num in nums if num % 2 == 0)

#2
def big_diff(nums):
  max_num = max(nums)
  min_num = min(nums)
  return max_num - min_num

#3
def centered_average(nums):
    nums.sort()  # Sort the array in ascending order
    nums = nums[1:-1]  # Ignore the first and last elements
    return sum(nums) // len(nums)  # Return the integer division of the sum and length of the array

#4
def sum13(nums):
    if not nums:
        return 0

    sum = 0
    skip_next = False
    for i in range(len(nums)):
        if nums[i] == 13:
            skip_next = True
        elif not skip_next:
            sum += nums[i]
        else:
            skip_next = False

    return sum

#5
def sum67(nums):
    sum = 0
    skip = False
    for num in nums:
        if num == 6:
            skip = True
        elif num == 7 and skip:
            skip = False
        elif not skip:
            sum += num
    return sum

#6
def has22(nums):
    has = False
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True

    return False