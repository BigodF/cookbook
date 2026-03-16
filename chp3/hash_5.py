from typing import List
from functools import cmp_to_key

class Solution:
    def twoSum_test(self, ):
        nums = [2,7,11,15]
        target = 9
        res = [0, 1]
        
        nums = [3,2,4]
        target = 6
        res = [1, 2]
        
        r = self.twoSum(nums, target)
        print(r)
        print(r==res)
        return
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n2i = {n: i for i, n in enumerate(nums)}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in n2i and i != n2i[t]:
                return [i, n2i[t]]
    
    # 15, https://leetcode.cn/problems/3sum/
    def threeSum_test(self, ):
        nums = [-1,0,1,2,-1,-4]
        res = [[-1,-1,2],[-1,0,1]]
        
        # nums = [0,1,1]
        # res = []
        
        # nums = [0,0,0]
        # res = [[0,0,0]]
        nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
        res = [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]

        r = self.threeSum_mo1(nums)
        print(r)
        print(r==res)
        return
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        n2i = {n: i for i, n in enumerate(nums)}
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            if x > 0:
                break
            for j in range(i+1, n - 1):
                y = nums[j]
                if j > i + 1 and y == nums[j-1]:
                    continue
                t = 0 - x - y
                if t < y:
                    break
                if t in n2i and n2i[t] > j:
                    res.append([x, y, t])
        return res
    def threeSum_mo1(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            if x > 0:
                break
            k = n - 1
            for j in range(i+1, n - 1):
                y = nums[j]
                if j > i + 1 and y == nums[j-1]:
                    continue
                t = 0 - x - y
                if t < y:
                    break
                while j < k and nums[k] > t:
                    k -= 1
                if j < k:
                    if nums[k] == t:
                        res.append([x, y, t])
                    if nums[k] < t:
                        k = min(k+1, n-1)
                else:
                    break
        return res
        

    # 41: https://leetcode.cn/problems/first-missing-positive/
    def test(self, ):
        nums = [1,2,0]
        res = 3
        
        # nums = [3,4,-1,1]
        # res = 2
        
        # nums = [7,8,9,11,12]
        # res = 1

        r = self.firstMissingPositive_mo1(nums)
        print(r)
        print(r==res)
        return
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(n for n in nums if n > 0)
        l2r = {n:n for n in s}
        for n in s:
            if n in l2r:
                r = l2r[n]
                while r+1 in l2r:
                    r = l2r.pop(r+1)
                l2r[n] = r
        min_l, min_r = None, None
        for l, r in l2r.items():
            if min_l == None or l < min_l:
                min_l, min_r = l, r
        if min_l == 1:
            return min_r + 1
        else:
            return 1
    
    def firstMissingPositive_mo1(self, nums: List[int]) -> int:
        # 首先最小正整数的范围是：[1, n+1]
        # 第一步，负数置为>=n+1的数，目的是把负数空间清空，留给标记用
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        # 把[1, N]范围内的数，对应下标的元素，置为相反数，也就是负数。
        # 这样做的目的是：1. 标记此下标+1，在数组里出现过。
        # 2. 保留下标原来的数字，
        # 相当于把这两个信息，压缩到一个位置。
        for i in range(n):
            x = abs(nums[i])
            if 1 <= x <= n and nums[x-1] > 0:
                nums[x-1] = -nums[x-1]
        # 按位置查找，>0说明，数组里没有出现过该下标+1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
                
                
                
            
    # 128: https://leetcode.cn/problems/longest-consecutive-sequence/description/
    def longestConsecutive_test(self, ):
        nums = [100,4,200,1,3,2]
        res = 4
        
        nums = [0,3,7,2,5,8,4,6,0,1]
        res = 9
        
        nums = list(range(10))
        res = 10
        
        # nums = [0, -1]
        # res = 2

        r = self.longestConsecutive_union_search(nums)
        print(r)
        print(r==res)
        return
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        # 以n为起点遍历
        res = 0
        for n in nums:
            if n-1 not in s:
                _n = n + 1
                while _n in s:
                    _n += 1
                res = max(res, _n - n)
        return res
    def longestConsecutive_dp(self, nums: List[int]) -> int:
        dp = {} # dp[i]表示以i为左端点、或者右端点的最长连续子串。
        # 更新方式：如果i更新过了，就没必要更新了，
        # 存在i，并且没有更新过，此时dp[i-1]表示i-1为右端点的最长子串长度，dp[i+1]表示以i+1为左端点的最长子串长度。这两个子串可以合并。dp[i]可以为任意值。
        res = 0
        for n in nums:
            if n not in dp:
                left = dp.get(n-1, 0)
                right = dp.get(n+1, 0)
                L = left + right + 1
                # dp[n] = 1
                dp[n - left] = L
                dp[n + right] = L
                # 只是为了标记这个点已经处理过了，不会再产生新的区域
                dp[n] = L # 虽然dp[n]可以为任意值，但是left、right可能为0，会有覆盖问题，或者把这句放到最前面
                res = max(res, L)
        return res
    def longestConsecutive_dp0(self, nums: List[int]) -> int:
        hash_dict = dict()
        
        max_length = 0
        for num in nums:
            if num not in hash_dict:
                # 左边的数字刚刚已经告诉我了他的连续子序列长度，现在我需要拿出来和右边拼接了
                # 没告诉过我就说明他也不知道，那就是0
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                
                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length
                
                # 既然已经告诉旁边的人我的情况了，自然赋值是什么都不重要了
                hash_dict[num] = cur_length
                 # 告诉左边的数字我的右边连续子序列长度是cur_length（或者说只有他左边的数字需要他）
                hash_dict[num - left] = cur_length
                # 告诉右边的数字我的左边连续子序列长度是cur_length
                hash_dict[num + right] = cur_length
                
        return max_length
    def longestConsecutive_left(self, nums: List[int]) -> int:
        s = set(nums)
        # 以n为起点遍历
        res = 0
        for n in s:
            if n-1 not in s:
                _n = n + 1
                while _n in s:
                    _n += 1
                res = max(res, _n - n)
        return res
    def longestConsecutive_left_right(self, nums: List[int]) -> int:
        s = {n: n for n in nums} # left: right
        res = 0
        for n in nums:
            if n in s:
                r = s[n]
                # 找到新的右边界
                while r+1 in s:
                    # 删除非起点
                    r = s.pop(r+1)
                s[n] = r # 更新右边界
                res = max(r - n + 1, res)
        return res
    def longestConsecutive_union_search(self, nums: List[int]) -> int:
        class UnionFind:
            def __init__(self, nums) -> None:
                self.parent = {n: n for n in nums}
                pass
            def find(self, x):
                if x not in self.parent:
                    return None
                t = x
                while t != self.parent[t]:
                    t = self.parent[t]
                while x != self.parent[x]:
                    p = self.parent[x]
                    self.parent[x] = t
                    x = p
                return t
            def union(self, x, y):
                x_root = self.find(x)
                y_root =self.find(y)
                self.parent[x_root] = y_root
        uf = UnionFind(nums)
        for n in uf.parent:
            if uf.find(n+1) != None:
                uf.union(n, n+1)
        res = 0
        for n in uf.parent:
            p = uf.find(n)
            res = max(res, p - n + 1)
        return res

    
        
if __name__ == '__main__':
    Solution().test()