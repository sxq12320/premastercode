import numpy as np
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None :
            return l2
        if l2 is None:
            return l1
        
        prehead = ListNode(0) #创建一个val为0的单节点
        head = prehead #指针开始的地方
        carry = 0

        while l1 and l2: #同时
            retain = (l1.val + l2.val + carry)%10
            carry = (l1.val + l2.val + carry )//10
            head.next = ListNode(retain)
            l1 = l1.next
            l2 = l2.next
            head = head.next
        
        while l1: # l1 too long
            retain = (l1.val +carry)%10
            carry = (l1.val +carry)//10
            head.next = ListNode(retain)
            l1 = l1.next
            head = head.next
        
        while l2 :
            retain = (l2.val + carry)%10
            carry = (l2.val + carry)//10
            head.next = ListNode(retain)
            l2 = l2.next
            head = head.next
        
        if carry == 1:
            head.next  = ListNode(carry)

        return prehead.next    




# l1 = [2,4,3], l2 = [5,6,4]
l10 = ListNode(2)
l11 = ListNode(4)
l12 = ListNode(3)
l10.next = l11
l11.next = l12

l1 = l10
# while l1:
#     print(l1.val)
#     l1 = l1.next


l20 = ListNode(5)
l21 = ListNode(6)
l22 = ListNode(4)
l20.next = l21
l21.next = l22
l2 = l20

# while l2:
#     print(l2.val)
#     l2 = l2.next

res = Solution.addTwoNumbers(Solution , l1 , l2 )
while res:
    print(res.val)
    res = res.next







