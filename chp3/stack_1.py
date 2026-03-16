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


class MyQueue:

    def __init__(self):
        self.s0 = []
        self.s1 = []

    def push(self, x: int) -> None:
        self.s0.append(x)

    def pop(self) -> int:
        self.peek()
        if self.s1:
            return self.s1.pop()
        return -1
        

    def peek(self) -> int:
        if self.s1:
            return self.s1[-1]
        if not self.s0:
            return -1
        while self.s0:
            self.s1.append(self.s0.pop())
        return self.s1[-1]


    def empty(self) -> bool:
        return not self.s0 and not self.s1
    
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
    
    def calculate_test(self, ):
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
            # print(stack)
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
    
    def calculate_224_test(self, ):
        s = "1-(     -2)"
        res = "3"
        
        # s = "3/2"
        # res = 1
        
        # s = "3+5/2"
        # res = 5
        
        # s = '1-1+1'
        # res = 1
        
        r = self.calculate_224(s)
        print(r)
        print(r==res)

    def calculate_224(self, s: str) -> int:
        s = s.replace(' ', '')
        exp_list = self.to_suffix_exp(s)
        res = self.suffix_exp_cal(exp_list)
        
        
        # exp_list = self.to_prefix_exp(s)
        # res = self.prefix_exp_cal(exp_list)
        return res
    
    def MyQueue_test(self, ):
        ops = ["MyQueue", "push", "push", "peek", "pop", "empty"]
        args = [[], [1], [2], [], [], []]
        res = [None, None, None, 1, 1, False]

        ops = ["MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"]
        args = [[],[1],[2],[3],[4],[],[5],[],[],[],[]]
        res = [None,None,None,None,None,1,None,2,3,4,5]
        
        s = MyQueue()
        for i in range(1, len(ops)):
            op = ops[i]
            arg = args[i]
            r = res[i]
            if arg:
                _r = getattr(s, op)(arg[0])
            else:
                _r = getattr(s, op)()
            assert _r == r
    
    def decodeString_test(self, ):
        s = "3[a]2[bc]"
        res = "aaabcbc"
        
        # s = "3[a2[c]]"
        # res = "accaccacc"
        
        # s = "2[abc]3[cd]ef"
        # res = "abcabccdcdcdef"
        
        # s = "abc3[cd]xyz"
        # res = "abccdcdcdxyz"
        
        r = self.decodeString(s)
        print(r)
        print(r==res)

    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        i = 0
        n = len(s)
        while i < n:
            num = ''
            while '0' <= s[i] <= '9':
                num += s[i]
                i += 1
            if num:
                stack.append(int(num))
            
            c = s[i]
            if stack:
                if c == ']':
                    _s = ''
                    while stack[-1] != '[':
                        _s = stack.pop() + _s
                    stack.pop()
                    num = stack.pop()
                    _s = _s * num
                    if stack:
                        stack.append(_s)
                    else:
                        res += _s
                else:
                    stack.append(c)
            else:
                res += c
            i += 1
        if stack:
            res += stack[0]
        return res
    
    def test(self, ):
        s = "(()"
        res = 2
        
        s = ")()())"
        res = 4
        
        s = ""
        res = 0
        
        s = ")(())))(())())"
        res = 6
        
        s = "(()"
        res = 2
        
        r = self.longestValidParentheses_cnter(s)
        print(r)
        print(r==res)
        
    def longestValidParentheses(self, s: str) -> int:
        flag = [0] * len(s)
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')' and stack:
                flag[stack.pop()] = 1
                flag[i] = 1
        
        max_len = 0
        i = 0
        n = len(s)
        while i < n:
            cnt = 0
            while i < n and flag[i] == 1:
                cnt += 1
                i += 1
            i += 1
            max_len = max(max_len, cnt)
        return max_len
    
    def longestValidParentheses_stack(self, s: str) -> int:
        # 只保留一个最右边未匹配成功的)的位置
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                # 有两种可能：
                # 1. 匹配成功，pop之后stack[-1]是最右边未成功的，()都有可能。
                # 2. 匹配未成功，只有一种情况，就是stack[-1]是)，此时pop后为空。
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res
    
    def longestValidParentheses_dp(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        max_len = 0
        for i in range(1, n):
            c = s[i]
            if c == ')':
                if s[i-1] == '(':
                    t = 0 if i < 2 else dp[i-2]
                    dp[i] = t + 2
                else:
                    _i = i - dp[i-1] - 1
                    if _i >= 0 and s[_i] == '(':
                        t = 0 if _i < 1 else dp[_i - 1]
                        dp[i] = dp[_i-1] + dp[i-1] + 2
            max_len = max(max_len, dp[i])
        return max_len
    
    def longestValidParentheses_cnter(self, s: str) -> int:
        def cnt(s, reverse=False):
            l = r = 0
            if reverse:
                lc = ')'
            else:
                lc = '('
            max_len = 0
            for c in s:
                if c == lc:
                    l += 1
                else:
                    r += 1
                if r > l:
                    # )的个数不能大于(
                    l = r = 0
                elif r == l:
                    # 相等时，是有效子串，<时不一定是有效子串，所以需要反向遍历。
                    max_len = max(max_len, l + r)
                    
            # max_len = max(max_len, 2*min(l, r))
            return max_len
        return max(cnt(s), cnt(s[::-1], reverse=True))
                    
            
        
        
        
    
if __name__ == '__main__':
    s = Solution()
    s.test()
    # s.suffix_exp_cal([])