from typing import List
from functools import cmp_to_key
import heapq


class LRUCache:

    def __init__(self, capacity: int):
        import collections
        self.hash = {}
        self.dup_cnt = {}
        self.deque = collections.deque()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        v = self.hash[key]
        self.dup_cnt[key] += 1
        self.deque.append(key)
        return v
        
    # ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # [[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.dup_cnt[key] += 1
        else:
            if len(self.dup_cnt) >= self.capacity:
                while len(self.dup_cnt) >= self.capacity:
                    t = self.deque.popleft()
                    self.dup_cnt[t] -= 1
                    if self.dup_cnt[t] == 0:
                        self.dup_cnt.pop(t)
                        self.hash.pop(t)
            self.dup_cnt[key] = 1
        self.hash[key] = value
        self.deque.append(key)
        
        
            
        

class Solution:
    def threeSum_test(self, ):
        nums = [-1,0,1,2,-1,-4]
        res = [[-1,-1,2],[-1,0,1]]

        # nums = [0,0,0]
        # res = [[0, 0, 0]]

        # nums = [-100,-70,-60,110,120,130,160]
        # res = [[-100,-60,160],[-70,-60,130]]
        
        r = self.threeSum(nums)
        print(r)
        print(r==res)
        return

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        n = len(nums)
        res = []
        for i in range(n):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                while j < k and (j!=i+1 and  nums[j-1] == nums[j]):
                    j += 1
                k0 = 0 - (nums[i] + nums[j])
                while j < k and ((k!=n-1 and nums[k] == nums[k+1]) or nums[k] > k0):
                    k -= 1
                if j < k and nums[k] == k0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                j += 1
        return res
    
    def moveZeroes_test(self, ):
        nums = [0,1,0,3,12]
        res = [1,3,12,0,0]

        # nums = [1, 0]
        # res = [1, 0]

        self.moveZeroes(nums)
        print(nums)
        print(nums==res)
        return
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        n = len(nums)
        while r < n:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        print(l, r)

    def merge_test(self, ):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        res = [1,2,2,3,5,6]

        # nums1 = [1]
        # m = 1
        # nums2 = []
        # n = 0
        # res = [1]

        # nums1 = [0]
        # m = 0
        # nums2 = [1]
        # n = 1
        # res = [1]


        # nums = [1, 0]
        # res = [1, 0]

        self.merge(nums1, m, nums2, n)
        print(nums1)
        print(nums1==res)
        return
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = m + n - 1
        r0, r1 = m - 1, n - 1
        while True:
            while r0 >= 0 and (r1 < 0 or nums1[r0] >= nums2[r1]):
                nums1[r], nums1[r0] = nums1[r0], nums1[r]
                r0 -= 1
                r -= 1
            while r1 >= 0 and (r0 < 0 or nums1[r0] < nums2[r1]):
                nums1[r], nums2[r1] = nums2[r1], nums1[r]
                r1 -= 1
                r -= 1
            if r1 < 0 and r0 < 0:
                break
    
    def addStrings_test(self, ):
        num1 = "11"
        num2 = "123"
        res = "134"

        num1 = "456"
        num2 = "77"
        res = '533'

        r = self.addStrings(num1, num2)
        print(r)
        print(r==res)
        return
    
    def addStrings(self, num1: str, num2: str) -> str:
        r = max(len(num1), len(num2))
        t = 0
        res = ''
        for i in range(-1, -r-1, -1):
            a = 0 if -i > len(num1) else int(num1[i])
            b = 0 if -i > len(num2) else int(num2[i])
            c = a + b + t
            if c > 9:
                c -= 10
                t = 1
            else:
                t = 0
            res = str(c) + res
        if t:
            res = str(t) + res
        return res
    
    def maxSlidingWindow_test(self, ):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        res = [3,3,5,5,6,7]
        
        # nums = [1]
        # k = 1
        # res = [1]

        r = self.maxSlidingWindow_heap(nums, k)
        print(r)
        print(r==res)
        return
    def maxSlidingWindow_heap(self, nums: List[int], k: int) -> List[int]:
        heap = [(nums[i], i) for i in range(k-1)]
        heapq.heapify_max(heap)
        
        res = []
        for i in range(k-1, len(nums)):
            heapq.heappush_max(heap, (nums[i], i))
            while heap[0][1] < i - k + 1:
                heapq.heappop_max(heap)
            res.append(heap[0][0])
        return res
    def maxSlidingWindow_deque(self, nums: List[int], k: int) -> List[int]:
        import collections
        q = collections.deque()
        
        for i in range(k-1):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        
        res = []
        for i in range(k-1, len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            while q and q[0] < i - k + 1:
                q.popleft()
            res.append(nums[q[0]])
        return res
    def maxSlidingWindow_double_ptr(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_max = []
        for i in range(n):
            if i % k == 0:
                prefix_max.append(nums[i])
            else:
                prefix_max.append(max(prefix_max[i-1], nums[i]))
        
        suffix_max = [0] * n
        for i in range(n-1, -1, -1):
            if i == n-1 or i % k == k-1:
                suffix_max[i] = nums[i]
            else:
                suffix_max[i] = max(suffix_max[i+1], nums[i])
        
        res = [max(prefix_max[i], suffix_max[i-k+1]) for i in range(k-1, n)]
        return res
    
    
    def lengthOfLongestSubstring_test(self, ):
        s = "abcabcbb"
        res = 3
        
        # s = "bbbbb"
        # res = 1
        
        # s = "pwwkew"
        # res = 3

        r = self.lengthOfLongestSubstring1(s)
        print(r)
        print(r==res)
        return  
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        c2i = {}
        max_len = 0
        for j in range(len(s)):
            c = s[j]
            if c in c2i:
                _i = c2i[c] + 1
                for t in range(i, _i):
                    c2i.pop(s[t])
                i = _i
            c2i[c] = j
            max_len = max(max_len, len(c2i))
        return max_len
    
    def lengthOfLongestSubstring1(self, s: str) -> int:
        c2i = {}
        res, tmp = 0, 0
        for i in range(len(s)):
            c = s[i]
            _i = c2i.get(c, -1)
            c2i[c] = i
            tmp = tmp + 1 if tmp < i - _i else i - _i
            res = max(res, tmp)
        return res
    
    def findLength_test(self, ):
        nums1 = [1,2,3,2,1]
        nums2 = [3,2,1,4,7]
        res = 3
        
        # nums1 = [0,0,0,0,0]
        # nums2 = [0,0,0,0,0]
        # res = 5
        
        r = self.findLength(nums1, nums2)
        print(r)
        print(r==res)
        return  
    
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''dp_i_j = f(a[i:], b[j:])
        dp_i_j-1 = f(a[i:], b[j-1:]) = f(a[i:], b[j:])
        '''
        m, n = len(nums1), len(nums2)
        last_dp = [0] * (n+1)
        dp = [0] * (n+1)
        res = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[j+1] = last_dp[j] + 1
                    res = max(res, dp[j+1])
            last_dp = dp
            dp = [0] * (n+1)
        return res
        
    def minWindow_test(self, ):
        s = "ADOBECODEBANC"
        t = "ABC"
        res = 'BANC'
        
        # s = "a"
        # t = "a"
        # res = 'a'
        
        # s = "a"
        # t = "aa"
        # res = ''
        
        # nums1 = [0,0,0,0,0]
        # nums2 = [0,0,0,0,0]
        # res = 5
        

        r = self.minWindow(s, t)
        print(r)
        print(r==res)
        return  

    def minWindow(self, s: str, t: str) -> str:
        '''https://leetcode.cn/problems/minimum-window-substring/description/
        给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。

        测试用例保证答案唯一。
        
        '''
        def check(s_chr, t_chr):
            for c, n in t_chr.items():
                if s_chr.get(c, 0) < n:
                    return False
            return True
        
        def add(chr, c, x):
            if c not in chr:
                chr[c] = 0
            chr[c] += x
        
        t_chr = {}
        for c in t:
            if c in t_chr:
                t_chr[c] += 1
            else:
                t_chr[c] = 1
        m, n = len(s), len(t)
        l, r = 0, 0
        res_len = m + 1
        res = ''
        
        s_chr = {}
        while True:
            while r < m:
                add(s_chr, s[r], 1)
                r += 1
                if check(s_chr, t_chr):
                    break
                
            
            while l <= r:
                add(s_chr, s[l], -1)
                l += 1
                if not check(s_chr, t_chr):
                    l -= 1
                    add(s_chr, s[l], 1)
                    break
                
            if r <= m:
                if check(s_chr, t_chr) and res_len > r - l:
                    res_len = r - l
                    res = s[l: r]
            
            if r >= m:
                break
        return res
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        dp[i, j] = min(dp[i-1, j], dp[i, j-1]) + grid[i, j]
        '''
        
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * (n+1) for _ in range(2)]
        dp[0][1] = 0
        for i in range(m):
            last_i = i % 2
            cur_i = (i + 1) % 2
            for j in range(n):
                dp[cur_i][j+1] = min(dp[last_i][j+1], dp[cur_i][j]) + grid[i][j]
        return dp[m%2][-1]
    
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [list(range(n+1)) for _ in range(2)]
        for i in range(m):
            last_i = i % 2
            cur_i = (i + 1) % 2
            c1 = word1[i]
            dp[cur_i][0] = i + 1
            for j in range(n):
                c2 = word2[j]
                if c1 == c2:
                    dp[cur_i][j+1] = dp[last_i][j]
                else:
                    dp[cur_i][j+1] = min(dp[last_i][j], dp[cur_i][j], dp[last_i][j+1]) + 1
        return dp[m%2][-1]
    
    
    def longestValidParentheses_test(self, ):
        s = ")()())"
        res = 4
        
        s = '(()'
        res = 2
        
        s = "()(()"
        res = 2
        
        r = self.longestValidParentheses(s)
        print(r)
        print(r==res)
        return  
    def longestValidParentheses(self, s: str) -> int:
        def max_len(s, l_c='('):
            l_cnt = r_cnt = 0
            res = 0
            last_idx = 0
            for i, c in enumerate(s):
                if c == l_c:
                    l_cnt += 1
                else:
                    r_cnt += 1
                # print(l_cnt, r_cnt, res)
                if l_cnt == r_cnt:
                    res = max(res, 2*r_cnt)
                    last_idx = i
                elif l_cnt < r_cnt:
                    l_cnt = r_cnt = 0
            return res, last_idx
        res, l2r_idx = max_len(s, '(')
        if l2r_idx < len(s) - 1:
            r2l_max, _ = max_len(s[l2r_idx+1:][::-1], ')')
            res = max(res, r2l_max)
        
        return res
    
    def uniquePaths_test(self, ):
        m = 3
        n = 2
        res = 3
        
        r = self.uniquePaths(m, n)
        print(r)
        print(r==res)
        return
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        dp[i, j] = dp[i-1, j] + dp[i, j-1]
        # 初始化注意为0
        '''
        dp = [[0]*(n+1) for _ in range(2)]
        for i in range(m):
            last_i = i % 2
            cur_i = (i + 1) % 2
            dp[cur_i][1] = 1
            for j in range(1, n):
                dp[cur_i][j+1] = dp[cur_i][j] + dp[last_i][j+1]
        return dp[m%2][-1]
    
    def maxProduct_test(self, ):
        nums = [2,3,-2,4]
        nums = [-2,0,-1]
        print(self.maxProduct(nums))
    def maxProduct(self, nums: List[int]) -> int:
        '''
        dp[i, j] = dp[]
        '''
        last_max = last_min = nums[0]
        res = nums[0]
        for n in nums[1:]:
            _last_min = min(last_max*n, last_min*n, n)
            _last_max = max(last_max*n, last_min*n, n)
            last_max, last_min = _last_max, _last_min
            # print(last_max, last_min)
            res = max(res, last_max)
        return res
    
    def rob_test(self, ):
        nums = [1,2,3,1]
        nums = [2,7,9,3,1]
        print(self.rob(nums))
    def rob(self, nums: List[int]) -> int:
        '''
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        '''
        n = len(nums)
        dp = [0] * 3
        res = 0
        for i, n in enumerate(nums):
            __i = i % 3
            _i = (i + 1) % 3
            i = (i + 2) % 3
            
            # dp[i+2] = max(dp[i+1], dp[i]+n)
            dp[i] = max(dp[_i], dp[__i]+n)
            res = max(dp[i], res)
        return res
    
    def test(self, ):
        ops = ["LRUCache","put","put","get","put","get","put","get","get","get"]
        args = [[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
        
        ops = ["LRUCache","get","put","get","put","put","get","get"]
        args = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
        res = [None,-1,None,-1,None,None,2,6]
        
        lru = LRUCache(2)
        for i in range(1, len(ops)):
            op = ops[i]
            if i == len(ops) - 1:
                print()
            r = getattr(lru, op)(*args[i])
            print(op, args[i], r, r == res[i])
    
    
    def myAtoi(self, s: str) -> int:
       pos = True
       nums = False
       res = 0
       for c in s:
           if c == ' ':
               continue
           if first_char == False:
               if c in '-+':
                    first_char = True
                    if c == '-':
                        pos = False
                elif c in '++':
                    c
           
            
                
        
        
        
        
        

if __name__ == '__main__':
    Solution().test()