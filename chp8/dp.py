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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list2Tree(values):
    nodes = [TreeNode(val) if val!=None else None for val in values]
    n = len(values)
    head = None
    if nodes:
        layers = [nodes[0]]
        st = 1
        while st < n:
            _layers = [nodes[i+st] for i in range(2*len(layers)) if i+st < len(nodes)]
            for i, node in enumerate(layers):
                if 2*i < len(_layers):
                    node.left = _layers[2*i]
                if 2*i + 1 < len(_layers):
                    node.right = _layers[2*i+1]
            st += len(_layers)
            layers = [t for t in _layers if t]
        head = nodes[0]
    return head, nodes

def Tree2list(root):
    res = []
    def dfs(layer):
        _layer = []
        for n in layer:
            _layer.append(n.left)
            _layer.append(n.right)
        layer = [n for n in _layer if n]
        if layer:
            res.extend([n if n==None else n.val for n in _layer])
            dfs(layer)
    if root:
        res.append(root.val)
        dfs([root])
    return res

class Solution:
    def maxProfit_test(self, ):
        # prices = [7,1,5,3,6,4]
        # res = 5
        # r = self.maxProfit(prices)
        
        # prices = [7,1,5,3,6,4]
        # res = 7
        # prices = [7,1,5,3,6,4]
        # res = 7
        # r = self.maxProfit_2_dp(prices)
        
        # prices = [1,2,3,0,2]
        # res = 3
        # r = self.maxProfit_5_dp(prices)
        
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        res = 8
        r = self.maxProfit_6_dp(prices, fee)
        
        print(r)
        print(r==res)
        return
    # https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_value = prices[0]
        for p in prices[1:]:
            res = max(res, p-min_value)
            min_value = min(min_value, p)
        return res
    # https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/
    def maxProfit_2(self, prices: List[int]) -> int:
        '''
        贪心算法的正确性证明：
            1. 任意买点i、卖点j获得的利润p[i, j] = p[i, i+1] + p[i+1, i+2] + ... + p[j-1, j]
            2. 整个区间内，可以分解为任意相邻两天的利润。
            3. 如何获得最大利润呢，只需要正的利润即可。
        '''
        res = 0
        i = 0
        n = len(prices)
        while i < n:
            j = i
            while j + 1 < n and prices[j+1] >= prices[j]:
                j += 1
            res += prices[j] - prices[i]
            i = j + 1
        return res
    def maxProfit_2_dp(self, prices: List[int]) -> int:
        ''' 递推的状态包含两个，一个是天数i，另一个是该天是否有股票。
        定义：
            dp[i, 0]表示i天没有股票的最大利润。
            dp[i, 1]表示i天有股票的最大利润。
        
        转移过程：
            dp[i, 0] = max(dp[i-1, 0], dp[i-1, 1] + prices[i])
            dp[i, 1] = max(dp[i-1, 1], dp[i-1, 0] - prices[i])
        
        初始状态:
            dp[-1, 0] = 0
            dp[-1, 1] = -prices[0]
            或者从0开始
            dp[0, 0] = 0
            dp[0, 1] = -prices[0]
        '''
        d0 = 0
        d1 = -prices[0]
        for p in prices:
            _d0 = max(d0, d1+p)
            _d1 = max(d1, d0-p)
            d0, d1 = _d0, _d1
        return d0
    # https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
    def maxProfit_3_dp(self, prices: List[int]) -> int:
        '''

        '''
        k = 2
        buy_dp = [float('-inf')] * (k + 1) # 不存在的状态，让递推从sell_dp取值。
        sell_dp = [0] * (k + 1) # 虽然不存在的状态，但是符合要求，因为sell满足盈利为0，同时没有股票在手。
        for p in prices:
            for i in range(1, k+1):
                buy_dp[i] = max(buy_dp[i], sell_dp[i-1] - p)
                sell_dp[i] = max(sell_dp[i], buy_dp[i] + p)
        return max(sell_dp)
    # https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
    def maxProfit_5_dp(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [float('-inf')] * (n+2)
        sell = [0] * (n+2)
        for i, p in enumerate(prices):
            buy[i+2] = max(buy[i+1], sell[i]-p)
            sell[i+2] = max(sell[i+1], buy[i+2]+p)
        return sell[-1]
    # https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
    def maxProfit_6_dp(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = [float('-inf')] * (n+1)
        sell = [0] * (n+1)
        for i, p in enumerate(prices):
            buy[i+1] = max(buy[i], sell[i]-p-fee)
            sell[i+1] = max(sell[i], buy[i+1]+p)
        return sell[-1]
    
    # https://leetcode.cn/problems/single-number-ii/
    def singleNumber_3(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            for n in nums:
                if ((n >> i) & 1) > 0:
                    cnt += 1
            if cnt % 3:
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)
        return res
    # https://leetcode.cn/problems/single-number-iii/solutions/587516/zhi-chu-xian-yi-ci-de-shu-zi-iii-by-leet-4i8e/
    def singleNumber_2(self, nums: List[int]) -> List[int]:
        x = 0
        for n in nums:
            x ^= n
        x = x & -x
        a = b = 0
        for n in nums:
            if x & n > 0:
                a ^= n
            else:
                b ^= n
        return [a, b]
    
    # https://leetcode.cn/problems/find-the-duplicate-number/description/
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while slow == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    

    # https://leetcode.cn/problems/longest-increasing-subsequence/
    def lengthOfLIS_test(self,):
        nums = [10,9,2,5,3,7,101,18]
        res = 4
        r = self.lengthOfLIS(nums)
        
        print(r)
        print(r==res)
        return
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp[i]: 以i结尾的最长递增子序列。
        tail[i]: 长度为i+1的子序列的尾端的最小值。
        '''

        n = len(nums)
        tails =  [float('inf')] * (n + 1)
        dp = [1] * n
        
        res = 1
        def bs(t):
            '''
            查找小于t的最大下标
            '''
            l, r = 0, res + 1
            while l < r:
                m = (l + r) >> 1
                if tails[m] < t:
                    l = m + 1
                else:
                    r = m
            # 以上找到的l是>=t的最小下标，在左移一位就是<t的下标，注意有可能是-1。
            if tails[l] == t:
                l -= 1
            return l
        
        for i, t in enumerate(nums):
            min_len = bs(t)
            # min_len可能是-1，但是dp是用1处理化的，不影响结果。
            dp[i] = max(dp[i], min_len + 1)
            res = max(res, dp[i])
            tails[dp[i]-1] = min(tails[dp[i]-1], t)
        return res
    
    # https://leetcode.cn/problems/longest-common-subsequence/
    def test(self,):
        text1 = 'ABCBDAB'
        text2 = 'BACBBD'
        res = 4
        r = self.longestCommonSubsequence(text1, text2)
        
        print(r)
        print(r==res)
        return
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        dp[i, j]: 表示text1[:i] 和 text2[:j]最长公共子序列长度。
        递推过程：
        dp[i, j] = dp[i, j-1]

        '''
        # text1 = input().rstrip('.')
        # text2 = input().rstrip('.')
        m, n = len(text1), len(text2)
        dp1 = [0] * (n+1)
        dp2 = [0] * (n+1)
        max_len = -1
        max_cnt = 0
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp2[j+1] = dp1[j] + 1
                    # if dp2[j+1] > max_len:
                    #     max_len = dp2[j+1]
                    #     max_cnt = 1
                    # elif dp2[j+1] == max_len:
                    max_cnt += 1
                else:
                    dp2[j+1] = max(dp2[j], dp1[j+1])
            dp1 = dp2
            dp2 = [0] * (n+1)
        print(max_len)
        print(max_cnt)
        return max_len, max_cnt

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
    
    
    # def myAtoi(self, s: str) -> int:
    #    pos = True
    #    nums = False
    #    res = 0
    #    for c in s:
    #        if c == ' ':
    #            continue
    #        if first_char == False:
    #            if c in '-+':
    #                 first_char = True
    #                 if c == '-':
    #                     pos = False
    #             elif c in '++':
    #                 c
    
    def test(self,):
        nums = [3,2,1]
        print(self.nextPermutation(nums))
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = -1
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                idx = i - 1
                break
        if idx != -1:
            min_n_j = None
            min_j = None
            for j in range(idx+1, n):
                if nums[j] > nums[idx] and nums[j] <= min_n_j:
                    min_n_j = nums[j]
                    min_j = j
            nums[idx], nums[min_j] = nums[min_j], nums[idx]
        
        l = idx + 1
        r = n-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums


    
if __name__ == '__main__':
    Solution().test()