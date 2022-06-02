# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):
  def addTwoNumbers(self, l1, l2):
    # define a array
    l3 = []
    # for index, val in enumerate(l1 if len(l1) >= len(l2) else l2):
    #   l3.append(0)
    # traverse the l1 array sum two num
    for index, val in enumerate(l1):
      val1 = l1[index] if index+1 <= len(l1) else 0
      val2 = l2[index] if index+1 <= len(l2) else 0
      if len(l3) - index <= 0:
        l3.append(val1 + val2)
      else:
        l3[index] += (val1 + val2)
      if l3[index] > 9:
        l3.append(1)
        l3[index] -= 10
    return l3


class OtherSolution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode(0)
    result_tail = result
    carry = 0

    while l1 or l2 or carry:
      val1 = (l1.val if l1 else 0)
      val2 = (l2.val if l2 else 0)
      carry, out = divmod(val1+val2 + carry, 10)

      result_tail.next = ListNode(out)
      result_tail = result_tail.next

      l1 = (l1.next if l1 else None)
      l2 = (l2.next if l2 else None)

    return result.next


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

solution = OtherSolution()
print(solution.addTwoNumbers(l1, l2))
