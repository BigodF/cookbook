from typing import List
from functools import cmp_to_key

class Solution:
    # 5: https://leetcode.cn/problems/longest-palindromic-substring/
    def longestPalindrome_test(self, ):
        s = "babad"
        res = 'aba'
        
        # s = "cbbd"
        # res = 'bb'
        
        r = self.longestPalindrome_dp(s)
        print(r)
        print(r==res)
        return
    def longestPalindrome_dp(self, s: str) -> str:
        n = len(s)
        res = 0
        res_start = 0
        # 递推公式如下：
        # 1. 当i == j, dp[i, j] = True
        # 2. 当 i == j-1, 并且 s[i] == s[j], dp[i, j] = True
        # 3. 当 i == j-2, 并且 s[i] == s[j], dp[i, j] = True
        # 4. 当 i < j-2, 并且 s[i] == s[j], dp[i, j] = dp[i+1, j-1]
        # 条件可以合并为s[i] == s[j] and (j - i < 3 or dp[i+1, j-1]是为True，其余为False
        
        # 考虑简化空间使用，只有dp[i, j] = dp[i+1, j-1]这个条件会用到递推，而且i < j 。所以考虑先遍历j，在遍历i。遍历完i后，得到的dp是dp[:, j-1]，当给dp[i]（实际代表dp[i, j]）赋值时，dp[i+1]代表的是dp[i+1, j-1]，正好符合要求。
        dp = [False] * n
        for j in range(n):
            for i in range(j+1):
                # 合并条件
                if s[i] == s[j] and (j - i < 3 or dp[i+1]):
                    dp[i] = True
                else:
                    # 需要重新赋值，否则代表的是dp[i, j-1]
                    dp[i] = False
                if dp[i] and j - i + 1 > res:
                    # 更新
                    res = j - i + 1
                    res_start = i
        return s[res_start: res_start+res]
    def longestPalindrome_center_expand(self, s: str) -> str:
        n = len(s)
        def expand(l, r):
            cnt = r - l + 1
            while l - 1 >= 0 and r + 1 < n and s[l-1] == s[r+1]:
                l -= 1
                r += 1
                cnt += 2
            return l, r, cnt
        
        
        res = (0, 0)
        res_len = 1
        for i in range(n):
            _l, _r, _cnt = expand(i, i)
            if _cnt > res_len:
                res_len = _cnt
                res = (_l, _r)
            if i + 1 < n and s[i] == s[i+1]:
                _l, _r, _cnt = expand(i, i+1)
                if _cnt > res_len:
                    res_len = _cnt
                    res = (_l, _r)
        if res_len > 0:
            return s[res[0]: res[1]+1]
    
    # 151: https://leetcode.cn/problems/reverse-words-in-a-string/
    def reverseWords_test(self, ):
        s = "the sky is blue"
        res = "blue is sky the"
        
        s = "  hello world  "
        res = "world hello"
        
        # s = "a good   example"
        # res = "example good a"
        
        r = self.reverseWords(s)
        print(r)
        print(r==res)
        return
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = ''
        i = n - 1
        while i > -1:
            while i > -1 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
            j = i
            while j - 1 > -1 and s[j-1] != ' ':
                j -= 1
            res += s[max(j, 0):i+1] + ' '
            i = j - 1
        res = res[:-1]
        return res
    
    # 43: https://leetcode.cn/problems/multiply-strings/description/
    def multiply_test(self, ):
        num1 = "2"
        num2 = "3"
        res = "6"
        
        num1 = "123"
        num2 = "456"
        res = "56088"
        
        r = self.multiply(num1, num2)
        print(r)
        print(r==res)
        return
    def multiply(self, num1: str, num2: str) -> str:
        tmp_list = []
        for i, m in enumerate(num1[::-1]):
            t = 0
            tmp = '0' * i
            m = int(m)
            for n in num2[::-1]:
                n = int(n)
                c = m * n + t
                t = c // 10
                c = c % 10
                tmp = str(c) + tmp
            if t:
                tmp = str(t) + tmp
            tmp_list.append(tmp)
        
        res = tmp_list[0]
        for num in tmp_list[1:]:
            t = 0
            m, n = len(res), len(num)
            _res = ''
            res = res[::-1]
            num = num[::-1]
            for i in range(max(m, n)):
                c1 = int(res[i]) if i < m else 0
                c2 = int(num[i]) if i < n else 0
                c = c1 + c2 + t
                if c > 9:
                    t = 1
                    c = c - 10
                else:
                    t = 0
                _res = str(c) + _res
            if t:
                _res = str(t) + _res
            res = _res
        i = 0
        while i < len(res) and res[i] == '0':
            i += 1
        if i >= len(res):
            return '0'
        else:
            return res[i:]
        
    # 14: https://leetcode.cn/problems/longest-common-prefix/
    def test(self, ):
        num1 = "2"
        num2 = "3"
        res = "6"
        
        num1 = "123"
        num2 = "456"
        res = "56088"
        
        r = self.multiply(num1, num2)
        print(r)
        print(r==res)
        return 
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_list = [len(s) for s in strs]
        right = 0
        for i in range(min(len_list)):
            c = strs[0][i]
            for s in strs[1:]:
                if c != s[i]:
                    return s[:right]
            right += 1
        return strs[0][:right]
        
                
        
    
        
if __name__ == '__main__':
    Solution().test()