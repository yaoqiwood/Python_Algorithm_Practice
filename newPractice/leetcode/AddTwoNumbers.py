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


class NewOtherSolution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    resultList = ListNode(0)  # 初始化一个节点，用来返回最初的节点
    tempNodeList = resultList  # 使用其他变量接收这个初始化变量以及未来变化这个节点的位置指针
    temp = 0  # 对10取余的余数
    out = 0  # 若有进位则保存在这里
    while l1 or l2:  # 遍历循环这两个单链表
      val1 = l1.val if l1 else 0
      val2 = l2.val if l2 else 0
      # 对每一位相加并与进位相加并且对10取余 比如4+7=11 %10 则等于 1余1
      out, temp = divmod(val1 + val2 + out, 10)
      tempNodeList.val = temp  # 修改当前节点的值 将余数赋值

      # l1 l2 前进下一个节点
      l1 = l1.next if l1 is not None else None
      l2 = l2.next if l2 is not None else None

      # 对下一个节点赋予进位的初始值 这里有个逻辑判断 假设l1 和 l2 是最后一个节点，则需要将下一个节点为None
      tempNodeList.next = ListNode(out) if (
          out > 0 or ((l1 is not None) or (l2 is not None))) else None
      # 前进到下一个节点
      tempNodeList = tempNodeList.next

    # 返回初始节点 结束
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
