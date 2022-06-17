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


class NewSolution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    ans = 0
    i = 0
    temp = {}
    # traverse the array
    for j in range(len(s)):
      if s[j] in temp:
        i = max(temp[s[j]], i)
      temp[s[j]] = j
      ans = max(j-i, ans)
    print(ans+1)
    return ans+1


class PracticeSolution:
  def lengthOfLongestSubstring(self, s):
    i = 0
    ans = 0
    temp = {}
    for j in range(len(s)):
      if s[j] in temp:
        i = max(temp[s[j]], i)
      temp[s[j]] = j + 1
      ans = max(j - i + 1, ans)
      print(ans)
    return ans


# strN = "tmmzuxt"
# strN = "pwwkew"
# strN = "abcabcbb"
strN = "abcabcbb"

# strN = " "
# strN = "abba"
# strN = "au"
solution = PracticeSolution()
solution.lengthOfLongestSubstring(strN)
