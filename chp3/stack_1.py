from typing import List, Union
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
        
    def isValid_test(self, ):
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
    
    def test(self, ):
        s = "3+2*2"
        res = 7
        
        # s = "3/2"
        # res = 1
        
        s = "3+5/2"
        res = 5
        
        s = '1-1+1'
        res = 1
        
        r = self.calculate(s)
        print(r)
        print(r==res)
        
    def calculate(self, s: str) -> int:
        # exp_list = self.to_suffix_exp(s)
        # res = self.suffix_exp_cal(exp_list)
        
        
        exp_list = self.to_prefix_exp(s)
        res = self.prefix_exp_cal(exp_list)
        return res
    
    def to_suffix_exp_test(self, ):
        s = "a-b/c+(d-e)-f*g"
        res = 'a b c /-  d e -+ f g * -'
        
        s = s.replace(' ', '')
        res = res.replace(' ', '')
        
        r = self.to_suffix_exp(s)
        print(r)
        print(r==res)
        
    def to_suffix_exp(self, exp: str, return_list: bool = True) -> Union[str, List]:
        op2h = {'+': 0, '-': 0, '*': 1, '/': 1}
        res = []
        
        op_stack = []
        tmp = ''
        for i, c in enumerate(exp):
            if c == ' ':
                continue
            if c in op2h or c in '()':
                if tmp:
                    res.append(int(tmp))
                    tmp = ''
                
                if c == '(':
                    op_stack.append(c)
                elif c == ')':
                    while op_stack and op_stack[-1] != '(':
                        res.append(op_stack.pop())
                    op_stack.pop()
                else:
                    if c == '-' and (i == 0 or exp[i-1] == '('):
                        res.append(0)
                    while op_stack and op_stack[-1] != '(' and op2h[op_stack[-1]] >= op2h[c]:
                        res.append(op_stack.pop())
                    op_stack.append(c)
            else:
                tmp = tmp+c
        if tmp:
            res.append(int(tmp))
        while op_stack:
            res.append(op_stack.pop())
        if return_list:
            return res
        return ''.join([str(t) for t in res])
    
    def suffix_exp_cal(self, exp_list):
        # exp_list = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # exp_list = ["2","1","+","3","*"]
        # exp_list = ["4","13","5","/","+"]
        # exp_list = ["4","-2","/","2","-3","-","-"]
        stack = []
        for c in exp_list:
            if isinstance(c, str):
                y = stack.pop()
                x = stack.pop()
                    
                if c == '+':
                    z = x + y
                elif c == '-':
                    z = x - y
                elif c == '*':
                    z = x * y
                else:
                    z = x / y
                stack.append(z)
            else:
                stack.append(c)
            print(stack)
        return stack[0]
        
    
    def to_prefix_exp_test(self, ):
        s = "a-b/c+(d-e)-f*g"
        res = '- + - a / b c - d e * f g'
        
        s = s.replace(' ', '')
        res = res.replace(' ', '')
        
        r = self.to_prefix_exp(s)
        print(r)
        print(r==res)
        
    def to_prefix_exp(self, exp: str, return_list: bool = True) -> Union[str, List]:
        op2h = {'+': 0, '-': 0, '*': 1, '/': 1}
        res = []
        
        op_stack = []
        tmp = ''
        exp = exp[::-1]
        for i, c in enumerate(exp):
            if c == ' ':
                continue
            if c in op2h or c in '()':
                if tmp:
                    res.append(int(tmp))
                    tmp = ''
                
                if c == ')':
                    op_stack.append(c)
                elif c == '(':
                    while op_stack and op_stack[-1] != ')':
                        res.append(op_stack.pop())
                    op_stack.pop()
                else:
                    if c == '-' and (i + 1 >= len(exp) or exp[i+1] == '('):
                        res.append(0)
                    while op_stack and op_stack[-1] != ')' and op2h[op_stack[-1]] > op2h[c]:
                        res.append(op_stack.pop())
                    op_stack.append(c)
            else:
                tmp = c + tmp
        if tmp:
            res.append(int(tmp))
        while op_stack:
            res.append(op_stack.pop())
        res = res[::-1]
        if return_list:
            return res
        return ''.join([str(t) for t in res])

    def prefix_exp_cal(self, exp_list):
        stack = []
        for c in exp_list[::-1]:
            if isinstance(c, str):
                x = stack.pop()
                y = stack.pop()
                if c == '+':
                    z = x + y
                elif c == '-':
                    z = x - y
                elif c == '*':
                    z = x * y
                else:
                    z = x // y
                stack.append(z)
            else:
                stack.append(c)
        return stack[0]
    
    
    
    
if __name__ == '__main__':
    s = Solution()
    # s.test()
    s.suffix_exp_cal([])