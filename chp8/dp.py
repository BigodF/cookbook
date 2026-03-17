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
    def test(self, ):
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
            
    
    
if __name__ == '__main__':
    Solution().test()