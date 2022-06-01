class Solution:
  def twoSum(self, nums, target):
    # traverse the array
    for x1, v1 in enumerate(nums):
      for x2, v2 in enumerate(nums):
        if (x1 != x2) and (target == v1 + v2):
          return [x1, x2]

  def anotherTwoSum(self, nums, target):
    # traverse the array
    seen = {}
    for i, value in enumerate(nums):  # 1
      remaining = target - nums[i]  # 2

      if remaining in seen:  # 3
        return [i, seen[remaining]]  # 4
      else:
        seen[value] = i  # 5


list = [3, 2, 4]

solution = Solution()
print(solution.anotherTwoSum(list, 6))
