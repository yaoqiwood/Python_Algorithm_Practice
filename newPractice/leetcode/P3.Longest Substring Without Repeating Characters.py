"""
  Given a string s, find the length of the longest substring without repeating characters.

  Example 1:
  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.
  Example 2:

  Input: s = "bbbbb"
  Output: 1
  Explanation: The answer is "b", with the length of 1.
  Example 3:

  Input: s = "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with the length of 3.
  Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    ans = 0
    tempMap = {}
    strLen = len(s)
    for strInd in range(strLen):
      if s[strInd] in tempMap:
        i = max(i, tempMap[s[strInd]])
      ans = max(ans, strInd - i + 1)
      tempMap[s[strInd]] = strInd + 1
    print(ans)
    return ans


strN = "tmmzuxt"
solution = Solution()
solution.lengthOfLongestSubstring(strN)
