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
    def deleteDuplicates_test(self, ):
        head = [1,1,2]
        res = [1,2]
        
        head = [1,1,2,3,3]
        res = [1, 2, 3]
        
        
        head = list2linked_list(head)
        # res = list2linked_list(res)
        
        r = self.deleteDuplicates(head)
        
        r = linked_list2list(r)
        print(r)
        print(r==res)
        return
        
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        while tmp:
            t = tmp.next
            while t and t.val == tmp.val:
                t = t.next
            tmp.next = t
            tmp = tmp.next
        return head
    
    def deleteDuplicates_82_test(self, ):
        head = [1,2,3,3,4,4,5]
        res = [1,2,5]
        
        # head = [1,1,1,2,3]
        # res = [2, 3]
        
        
        head = list2linked_list(head)
        # res = list2linked_list(res)
        
        r = self.deleteDuplicates_82(head)
        
        r = linked_list2list(r)
        print(r)
        print(r==res)
        return
    
    def deleteDuplicates_82(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        last = None # tmp的前一个node
        while tmp:
            x = tmp.next
            while x and x.val == tmp.val:
                x = x.next
            # x为空，或者x.val != tmp.val
            
            if x == tmp.next: # 无重复
                last = tmp
            else: # 有重复
                if last:
                    last.next = x
                else:
                    head = x
            tmp = x
        return head
    
    def reverseList_test(self, ):
        head = [1,2,3,4,5]
        
        # head = [1,2]
        
        res = head[::-1]
        
        
        head = list2linked_list(head)
        # res = list2linked_list(res)
        
        r = self.reverseList(head)
        
        r = linked_list2list(r)
        print(r)
        print(r==res)
        return
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        last_node = None
        while tmp:
            next_node = tmp.next
            tmp.next = last_node
            last_node = tmp
            tmp = next_node
        
        head = last_node
        return head
    
    def reverseBetween_test(self, ):
        head = [1,2,3,4,5]
        left = 2
        right = 4
        res = [1,4,3,2,5]
        
        head = [5]
        left = 1
        right = 1
        res = [5]
        
        
        head = list2linked_list(head)
        # res = list2linked_list(res)
        
        r = self.reverseBetween(head, left, right)
        
        r = linked_list2list(r)
        print(r)
        print(r==res)
        return
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        _head = None
        _head_left = None
        for _ in range(left):
            _head_left = _head
            if _head:
                _head = _head.next
            else:
                _head = head
        last = None
        tmp = _head
        for _ in range(right - left + 1):
            next_node = tmp.next
            tmp.next = last
            last = tmp
            tmp = next_node
        _head.next = tmp
        if _head_left:
            _head_left.next = last
        else:
            head = last
        return head
    
    def isPalindrome_test(self, ):
        head = [1,2,2,1]
        res = True
        
        # head = [1, 2]
        # res = False
        
        
        head = list2linked_list(head)
        # res = list2linked_list(res)
        
        r = self.isPalindrome(head)
        
        # r = linked_list2list(r)
        print(r)
        print(r==res)
        return
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cnt = 0
        tmp = head
        while tmp:
            cnt += 1
            tmp = tmp.next
        pal_len = cnt // 2
        if pal_len == 0:
            return True
        
        left_num = pal_len + 2 if cnt % 2 else pal_len + 1
        r_head = head
        for _ in range(left_num-1):
            r_head = r_head.next
        
        last = None
        tmp = r_head
        for _ in range(pal_len):
            next_node = tmp.next
            tmp.next = last
            last = tmp
            tmp = next_node
        r_head = last
        
        for _ in range(pal_len):
            if head.val != r_head.val:
                return False
            head = head.next
            r_head = r_head.next
        return True
    
    def reverseKGroup_test(self, ):
        head = [1,2,3,4,5]
        k = 2
        res = [2,1,4,3,5]
        
        head = [1,2,3,4,5]
        k = 3
        res = [3,2,1,4,5]
        
        
        head = list2linked_list(head)
        
        r = self.reverseKGroup(head, k)
        
        r = linked_list2list(r)
        print(r)
        print(r==res)
        return
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_group(head, k):
            tmp = head
            cnt = 0
            while cnt < k and tmp:
                cnt += 1
                tmp = tmp.next
            if cnt < k:
                return head, None, tmp
            tmp = head
            last = None
            cnt = 0
            while cnt < k:
                cnt += 1
                next_node = tmp.next
                tmp.next = last
                last = tmp
                tmp = next_node
            return last, head, tmp
        
        last_group_end = None
        group_head = head
        while group_head:
            _group_head, _group_end, next_group_head = reverse_group(group_head, k)
            
            if last_group_end == None:
                head = _group_head
            else:
                last_group_end.next = _group_head
            last_group_end = _group_end
            group_head = next_group_head
        return head
    
    def sortList_test(self, ):
        head = [4,2,1,3]
        head = [-1,5,3,4,0]
        head = []
        res = sorted(head)
        
        head = list2linked_list(head)
        
        r = self.sortList(head)
        
        r = linked_list2list(r)
        print(r)
        print(r==res)
        return
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(head, n):
            if n == 1:
                head.next = None
                return head
            m = n // 2
            l = head
            r = head
            for _ in range(m):
                r = r.next
            l_head = dfs(l, m)
            r_head = dfs(r, n - m)
            l_tmp = l_head
            r_tmp = r_head
            new_head = last = None
            while l_tmp or r_tmp:
                while l_tmp and (r_tmp == None or l_tmp.val <= r_tmp.val):
                    if last:
                        last.next = l_tmp
                    last = l_tmp
                    if new_head == None:
                        new_head = l_tmp 
                    l_tmp = l_tmp.next
                while r_tmp and (l_tmp == None or r_tmp.val < l_tmp.val):
                    if last:
                        last.next = r_tmp
                    last = r_tmp
                    if new_head == None:
                        new_head = r_tmp 
                    r_tmp = r_tmp.next
            last.next = None
            return new_head
        cnt = 0
        tmp = head
        while tmp:
            cnt += 1
            tmp = tmp.next
        if cnt >= 0:
            head = dfs(head, cnt)
        return head
    
    def mergeTwoLists_test(self, ):
        l1 = [1,2,4]
        l2 = [1,3,4]
        
        # l1 = []
        # l2 = []
        
        # l1 = []
        # l2 = [0]
        res = sorted(l1 + l2)
        
        l1 = list2linked_list(l1)
        l2 = list2linked_list(l2)
        
        
        r = self.mergeTwoLists(l1, l2)
        
        r = linked_list2list(r)
        print(r)
        print(r==res)
        return
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 != None:
            head = list2
        elif list1 != None and list2 == None:
            head = list1
        elif list1 and list2:
            if list1.val <= list2.val:
                head = list1
            else:
                head = list2
        else:
            head = None
        
        l_tmp = list1
        r_tmp = list2
        last = None
        while l_tmp or r_tmp:
            while l_tmp and (r_tmp == None or l_tmp.val <= r_tmp.val):
                if last:
                    last.next = l_tmp
                last = l_tmp
                l_tmp = l_tmp.next
            while r_tmp and (l_tmp == None or r_tmp.val < l_tmp.val):
                if last:
                    last.next = r_tmp
                last = r_tmp
                r_tmp = r_tmp.next
        if last:
            last.next = None
        return head
    
    def test(self, ):
        lists = [[1,4,5],[1,3,4],[2,6]]
        res = [1,1,2,3,4,4,5,6]
        
        # lists = []
        # res = []
        
        # lists = []
        # res = []
        
        lists = [list2linked_list(t) for t in lists]
        
        r = self.mergeKLists(lists)
        
        r = linked_list2list(r)
        print(r)
        print(r==res)
        return
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = last = None
        while True:
            smallest_node = None
            smallest_idx = None
            for i, node in enumerate(lists):
                if node and (smallest_node == None or smallest_node.val > node.val):
                    smallest_node = node
                    smallest_idx = i
            if smallest_idx == None:
                break
            lists[smallest_idx] = smallest_node.next
            if head == None:
                head = smallest_node
            if last:
                last.next = smallest_node
            last = smallest_node
        return head
            
                    
                
            
        
        
            
            
        
        
        
        
                
                

if __name__ == '__main__':
    Solution().test()