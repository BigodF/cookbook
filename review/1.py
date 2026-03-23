from typing import List, Optional
from functools import cmp_to_key, cache

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
        nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        res = [1,2,3,4,8,12,11,10,9,5,6,7]
        
        nums = [[6,9,7]]
        res = [6,9,7]
        
        r = self.spiralOrder(nums)
        print(r)
        print(r==res)
        return
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        res = []
        while True:
            for j in range(left, right+1):
                res.append(matrix[top][j])
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            if top < bottom and left < right:
                for j in range(right-1, left-1, -1):
                    res.append(matrix[bottom][j])
                for i in range(bottom-1, top, -1):
                    res.append(matrix[i][left])
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1
            if top > bottom or left > right:
                break
        return res
    
    # def rotate(self, matrix: List[List[int]]) -> None:
    def test(self,):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        matrix = [
            [5,1,9,11],
            [2,4,8,10],
            [13,3,6,7],
            [15,14,12,16]
        ]
        
        n = len(matrix)
        for l in range(n, 1, -2):
            i = (n - l) // 2
            for j in range(i, i + l-1):
                tmp = matrix[i][j]
                matrix[j][n-i-1], tmp = tmp, matrix[j][n-i-1]
                matrix[n-i-1][n-j-1], tmp = tmp, matrix[n-i-1][n-j-1]
                matrix[n-j-1][i], tmp = tmp, matrix[n-j-1][i]
                matrix[i][j] = tmp
            for t in matrix:
                print(t)
    # def sortArray(self, nums: List[int]) -> List[int]:
    def test(self, ):
        nums = [5,2,3,1]
        nums = [5,1,1,2,0,0]
        def qs(l, r):
            if l >= r:
                return
            base = nums[l]
            l0, r0 = l, r
            l += 1
            while True:
                while l <= r and nums[l] <= base:
                    l += 1
                while l <= r and nums[r] > base:
                    r -= 1
                if l > r:
                    break
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            l -= 1
            nums[l0], nums[l] = nums[l], nums[l0]
            qs(l0, l-1)
            qs(l+1, r0)
            
        def qs1(l, r):
            if l >= r:
                return
            base = nums[l]
            l0, r0 = l, r
            less_i = l+1
            for i in range(l+1, r+1):
                if nums[i] <= base:
                    nums[i], nums[less_i] = nums[less_i], nums[i]
                    less_i += 1
            less_i -= 1
            nums[l0], nums[less_i] = nums[less_i], nums[l0]
            qs1(l0, less_i-1)
            qs1(less_i+1, r0)
            
        qs1(0, len(nums)-1)
        
        print(nums)
        
    # def search(self, nums: List[int], target: int) -> int:
    def test(self, ):
        nums = [4,5,6,7,0,1,2]
        target = 0

        import bisect
        bisect.bisect_left
    
    def test(self, ):
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        target = 7
        nums = [2,3,1,2,4,3]
        
        target = 11
        nums = [1,1,1,1,1,1,1,1]
        
        target = 4
        nums = [1,4,4]
        
        n = len(nums)
        l = 0
        r = 0
        s = 0
        res = float('inf')
        while r < n:
            while r < n and s + nums[r] < target:
                s += nums[r]
                r += 1
            
            if r < n:
                s += nums[r]
                # _s = s
                while l < r and s - nums[l] >= target:
                    s -= nums[l]
                    l += 1
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
            r += 1
        if res > n:
            res = 0
            
        print(res)
        return res
    
    # def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
    def test(self,):
        digits = ["1","3","5","7"]
        n = 100
        
        s = str(n)
        s_len = len(str(n))
        @cache
        def f(i: int, is_limit: bool, is_num: bool):
            if i >= s_len:
                return int(is_num)
            res = 0
            if not is_num:
                res += f(i+1, False, False)
            up = digits[i] if is_limit else '9'
            for d in digits:
                if d > up:
                    break
                res += f(i+1, is_limit and d == up, True)
            return res
        res = f(0, True, False)
        print(res)
        return res
        
        
        
if __name__ == '__main__':
    Solution().test()