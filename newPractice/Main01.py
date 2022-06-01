class Solution:
  def twoSum(self, nums, target):
    # traverse the array
    for x1, v1 in enumerate(nums):
      for x2, v2 in enumerate(nums):
        if (x1 != x2) and (target == v1 + v2):
          return [x1, x2]


list = [3, 2, 4]

solution = Solution()
solution.twoSum(list, 6)
