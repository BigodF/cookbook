from typing import List
from functools import cmp_to_key
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
    
    
class Solution:
    def MinStack_test(self, ):
        ops = ["MinStack","push","push","push","getMin","pop","top","getMin"]
        args = [[],[-2],[0],[-3],[],[],[],[]]
        res = [None,None,None,None,-3,None,0,-2]
        
        s = MinStack()
        for i in range(1, len(ops)):
            op = ops[i]
            arg = args[i]
            r = res[i]
            if arg:
                _r = getattr(s, op)(arg[0])
            else:
                _r = getattr(s, op)()
            assert _r == r
        
    def test(self, ):
        s = "()"
        res = True
        
        # s = "()[]{}"
        # res = True
        
        # s = "(]"
        # res = False
        
        # s = "([])"
        # res = True
        
        # s = "([)]"
        # res = False
        
        r = self.isValid(s)
        print(r)
        print(r==res)
        
        
        
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                _c = stack.pop()
                if (c == ')' and _c != '(') or (c == ']' and _c != '[') or (c == '}' and _c != '{'):
                    return False
        if stack:
            return False
        return True        

if __name__ == '__main__':
    Solution().test()