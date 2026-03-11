from typing import List, Optional
from functools import cmp_to_key

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2linked_list(nums):
    head = tmp = None
    node_list = []
    for t in nums:
        if tmp == None:
            tmp = ListNode(t)
            head = tmp
        else:
            tmp.next = ListNode(t)
            tmp = tmp.next
        node_list.append(tmp)
    return head, node_list

def linked_list2list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

class Solution:
    def hasCycle_test(self, ):
        head = [1,1,2]
        res = [1,2]
        
        head = [1,1,2,3,3]
        res = [1, 2, 3]
        
        
        head, node_list = list2linked_list(head)
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
    
    def detectCycle_test(self, ):
        head = [3,2,0,-4]
        pos = 1
        
        # head = [1,2]
        # pos = 0
        
        # head = [1]
        # pos = -1
        
        head = [1,2]
        pos = -1
        
        head, node_list = list2linked_list(head)
        # res = list2linked_list(res)
        res = None
        if pos >= 0:
            node_list[-1].next = node_list[pos]
            res = node_list[pos]
        
        r = self.detectCycle(head)
        
        print(r)
        print(r==res)
        return
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast:
            if not fast.next or not fast.next.next:
                return
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
    
    def getIntersectionNode_test(self, ):
        listA = [4,1]
        listB = [5,6,1]
        t = [8,4,5]
        
        # listA = [1,9,1]
        # listB = [3]
        # t = [2,4]
        
        # listA = [2,6,4]
        # listB = [1,5]
        # t = []
        
        listA, listA_list = list2linked_list(listA)
        listB, listB_list = list2linked_list(listB)
        t, t_list = list2linked_list(t)
        listA_list[-1].next = t
        listB_list[-1].next = t
        
        r = self.getIntersectionNode(listA, listB)
        
        print(r)
        print(r==t)
        return
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        a_isA, b_isB = True, True
        while a and b:
            if a == b:
                return a
            
            if a.next == None and a_isA:
                a = headB
                a_isA = False
            else:
                a = a.next

            if b.next == None and b_isB:
                b = headA
                b_isB = False
            else:
                b = b.next
        return
    
    def removeNthFromEnd_test(self, ):
        head = [1,2,3,4,5]
        n = 2
        
        # head = [1]
        # n = 1
        
        # head = [1, 2]
        # n = 1
        
        _n = len(head) - n
        res = head[:_n] + head[_n+1:]
        head, _ = list2linked_list(head)
        
        r = self.removeNthFromEnd(head, n)
        r = linked_list2list(r)
        print(r)
        print(r == res)
        return
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        for i in range(n-1):
            first = first.next
            
        last = None
        while first.next:
            first = first.next
            last = second
            second = second.next
        if last:
            last.next = second.next
        else:
            head = second.next
        return head
    
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        first = head
        second = head
        for i in range(cnt-1):
            first = first.next
            
        while first.next:
            first = first.next
            second = second.next
        return second
    
    def reorderList_test(self, ):
        head = [1,2,3,4]
        res = [1,4,2,3]
        
        # head = [1,2,3,4,5]
        # res = [1,5,2,4,3]
        
        head, _ = list2linked_list(head)
        
        r = self.reorderList(head)
        r = linked_list2list(r)
        print(r)
        print(r == res)
        return
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        from collections import deque
        q = deque()
        tmp = head
        while tmp.next:
            tmp = tmp.next
            q.append(tmp)
        
        tmp = head
        right = True
        while q:
            if right:
                t = q.pop()
            else:
                t = q.popleft()
            tmp.next = t
            tmp = t
            right = not right
        tmp.next = None
        return head
    
    def test(self, ):
        l1 = [2,4,3]
        l2 = [5,6,4]
        res = [7,0,8]
        
        # l1 = [0]
        # l2 = [0]
        # res = [0]
        
        # l1 = [9,9,9,9,9,9,9]
        # l2 = [9,9,9,9]
        # res = [8,9,9,9,0,0,0,1]
        
        l1, _ = list2linked_list(l1)
        l2, _ = list2linked_list(l2)
        
        r = self.addTwoNumbers(l1, l2)
        r = linked_list2list(r)
        print(r)
        print(r == res)
        return
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t = 0
        a, b = l1, l2
        last = head = None
        while a or b:
            x = 0
            if a:
                x = a.val
                a = a.next
            y = 0
            if b:
                y = b.val
                b = b.next
            c = x + y + t
            if c > 9:
                t = 1
                c -= 10
            else:
                t = 0
            node = ListNode(c)
            if last:
                last.next = node
            if head == None:
                head = node
            last = node
        if t:
            last.next = ListNode(t)
        return head
            
                
        
                
            
        

if __name__ == '__main__':
    Solution().test()