from typing import List
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

class MyStack:

    def __init__(self):
        from collections import deque
        self.q0 = deque()

    def push(self, x: int) -> None:
        self.q0.append(x)
        for _ in range(len(self.q0)-1):
            self.q0.append(self.q0.popleft())

    def pop(self) -> int:
        return self.q0.popleft() if self.q0 else -1

    def top(self) -> int:
        return self.q0[0] if self.q0 else -1
        
    def empty(self) -> bool:
        return len(self.q0) == 0
        


class Solution:
    # 42: https://leetcode.cn/problems/trapping-rain-water/description/
    def trap_test(self, ):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        res = 6
        
        height = [4,2,0,3,2,5]
        res = 9
        
        r = self.trap_pnt(height)
        print(r)
        print(r==res)
        return
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * (n + 1)
        right_max = [0] * (n + 1)
        for i in range(n):
            left_max[i+1] = max(left_max[i], height[i])
        for i in range(n-1, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        res = 0
        for i in range(n):
            a = min(left_max[i+1], right_max[i])
            if a > height[i]:
                res += a - height[i]
        return res
    def trap_pnt(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        lm = height[0]
        rm = height[-1]
        res = 0
        while l <= r:
            if lm >= rm:
                res += rm - height[r]
                r -= 1
                rm = max(rm, height[r])
            else:
                res += lm - height[l]
                l += 1
                lm = max(lm, height[l])
        return res
    
    
    # 
    def MyStack_test(self, ):
        ops = ["MyStack","push","push","top","pop","empty"]
        args = [[],[1],[2],[],[],[]]
        res = [None,None,None,2,2,False]
        
        s = MyStack()
        for i in range(1, len(ops)):
            op = ops[i]
            arg = args[i]
            r = res[i]
            if arg:
                _r = getattr(s, op)(arg[0])
            else:
                _r = getattr(s, op)()
            assert _r == r    
        
    def trap_test(self, ):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        res = 6
        
        height = [4,2,0,3,2,5]
        res = 9
        
        r = self.trap_pnt(height)
        print(r)
        print(r==res)
        return
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
if __name__ == '__main__':
    Solution().test()