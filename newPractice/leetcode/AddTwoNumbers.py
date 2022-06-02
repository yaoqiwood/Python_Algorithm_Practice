# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


def traverseRead(linkListNode):
  tempList = linkListNode
  while tempList:
    print(tempList.val)
    tempList = tempList.next


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
    resultList = ListNode(0)
    tempNodeList = resultList
    temp = 0
    out = 0
    while l1 or l2:
      val1 = l1.val if l1 else 0
      val2 = l2.val if l2 else 0
      out, temp = divmod(val1 + val2 + out, 10)
      tempNodeList.val = temp
      tempNodeList.next = ListNode(out) if (
          out > 0 or ((l1 and l1.next is not None) or (l2 and l2.next is not None))) else None
      tempNodeList = tempNodeList.next

      l1 = l1.next if l1 is not None else None
      l2 = l2.next if l2 is not None else None

    return resultList


# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(1)

l2 = ListNode(9)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
# l1.traverseRead()

solution = OtherSolution()
traverseRead(solution.addTwoNumbers(l1, l2))
