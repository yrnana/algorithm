# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        node = head
        while node:
            num *= 10
            num += node.val
            node = node.next
        return int(str(num), 2)
