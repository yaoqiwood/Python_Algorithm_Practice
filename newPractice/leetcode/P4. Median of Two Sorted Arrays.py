'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''


class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    temp = []
    outnum = 0
    for index, val in enumerate(nums1):
      temp.append(val)
    for index, val in enumerate(nums2):
      temp.append(val)

    temp = sorted(temp)
    middleIndex = len(temp) % 2
    middleIndexNum = int((len(temp) - 1) / 2)
    if middleIndex == 0:
      outnum = (temp[middleIndexNum] + temp[middleIndexNum + 1]) / 2.0
    else:
      outnum = temp[middleIndexNum]/1.0

    return outnum
    # print(temp)
    # print(middleIndex)


nums1 = [3, 4]
nums2 = [1, 2]

solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))
