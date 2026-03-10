from typing import List, Optional
from functools import cmp_to_key

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2linked_list(nums):
    head = tmp = None
    for t in nums:
        if tmp == None:
            tmp = ListNode(t)
            head = tmp
        else:
            tmp.next = ListNode(t)
            tmp = tmp.next
    return head

def linked_list2list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

class Solution:
    def test(self, ):
        head = [1,1,2]
        res = [1,2]
        
        head = [1,1,2,3,3]
        res = [1, 2, 3]
        
        
        head = list2linked_list(head)
        # res = list2linked_list(res)
        
        r = self.hasCycle(head)
        
        r = linked_list2list(r)
        print(r)
        print(r==res)
        return
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
               return False
            slow = slow.next
            fast = fast.next.next

        return False