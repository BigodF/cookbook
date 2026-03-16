from typing import List, Optional
from functools import cmp_to_key
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
    # 200: https://leetcode.cn/problems/number-of-islands/
    # 695: https://leetcode.cn/problems/max-area-of-island/description/
    def numIslands_test(self, ):
        grid = [
            ['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','0','0','0','0']
        ]
        res = 1
        
        # grid = [
        #     ['1','1','0','0','0'],
        #     ['1','1','0','0','0'],
        #     ['0','0','1','0','0'],
        #     ['0','0','0','1','1']
        # ]
        # res = 3
        
        grid = [["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]
        res = 58
        
        # grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        # res = 6
        
        r = self.numIslands_bfs(grid)
        print(r)
        print(r==res)
        return
    def numIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # visited = [[False]]
        def dfs(i, j):
            if i < 0 or i >= m or j <0 or j >= n:
                return 0
            c = grid[i][j]
            if c == 0:
                return 0
            if c == 1:
                grid[i][j] = 0
            cnt = 1
            cnt += dfs(i, j-1)
            cnt += dfs(i, j+1)
            cnt += dfs(i+1, j)
            cnt += dfs(i-1, j)
            return cnt
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                area = dfs(i, j)
                res = max(res, area)
        return res
    
    def numIslands_office(self, grid: List[List[str]]) -> int:
        import collections
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    area = 0
                    while neighbors:
                        row, col = neighbors.popleft()
                        area += 1
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"
                    print(r, c, area)
                    
        
        return num_islands
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        import copy, collections
        res_office = self.numIslands_office(copy.deepcopy(grid))
        print('\n\n')
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for t in grid:
                    print(t)
                grid[i][j] = '0'
                _i, _j = i, j
                stack = [(i, j)]
                # stack = collections.deque([(i, j)])
                res += 1
                area = 0
                while stack:
                    area += 1
                    # _i, _j = stack.pop()
                    # # _i, _j = stack.popleft()
                    # for x, y in [(_i-1, _j), (_i+1, _j), (_i, _j-1), (_i, _j+1)]:
                    
                    i, j = stack.pop()
                    
                    print(i, j)
                    # _i, _j = stack.popleft()
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0<=x<m and 0<=y<n and grid[x][y]=='1':
                            grid[x][y] = '0'
                            stack.append((x, y))
                print(_i, _j, area)
        # print(res_office, res)
        return res
    
    # 129: https://leetcode.cn/problems/sum-root-to-leaf-numbers/
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root, p_num):
            if not root:
                return
            p_num = p_num * 10 + root.val
            if root.left==None and root.right==None:
                nonlocal res
                res += p_num
                return
            dfs(root.left, p_num)
            dfs(root.right, p_num)
        dfs(root, 0)
        return res
    
    # 543: https://leetcode.cn/problems/diameter-of-binary-tree/
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            if not root:
                return -1
            left_deep = dfs(root.left)
            right_deep = dfs(root.right)
            nonlocal res
            res = max(res, left_deep + right_deep + 2)
            return max(left_deep, right_deep) + 1
        dfs(root)
        return res
    
    # 662: https://leetcode.cn/problems/maximum-width-of-binary-tree/description/
    def widthOfBinaryTree_test(self,):
        root = [1,3,2,5,3,None,9]
        res = 4
        
        # root = [1,3,2,5,None,None,9,6,None,7]
        # res = 7
        
        # root = [1,3,2,5]
        # res = 2
        
        root = [-64,12,18,-4,-53,None,76,None,-51,None,None,-93,3,None,-31,47,None,3,53,-81,33,4,None,-51,-44,-60,11,None,None,None,None,78,None,-35,-64,26,-81,-31,27,60,74,None,None,8,-38,47,12,-24,None,-59,-49,-11,-51,67,None,None,None,None,None,None,None,-67,None,-37,-19,10,-55,72,None,None,None,-70,17,-4,None,None,None,None,None,None,None,3,80,44,-88,-91,None,48,-90,-30,None,None,90,-34,37,None,None,73,-38,-31,-85,-31,-96,None,None,-18,67,34,72,None,-17,-77,None,56,-65,-88,-53,None,None,None,-33,86,None,81,-42,None,None,98,-40,70,-26,24,None,None,None,None,92,72,-27,None,None,None,None,None,None,-67,None,None,None,None,None,None,None,-54,-66,-36,None,-72,None,None,43,None,None,None,-92,-1,-98,None,None,None,None,None,None,None,39,-84,None,None,None,None,None,None,None,None,None,None,None,None,None,-93,None,None,None,98]
        res = 169
        
        root, node_list = list2Tree(root)
        r = self.widthOfBinaryTree(root)
        # r_list = Tree2list(r)
        print(r)
        print(res == r)
        return
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        def dfs(layer):
            _layer = []
            for n, i in layer:
                if n.left != None:
                    _layer.append((n.left, 2*i+1))
                if n.right != None:
                    _layer.append((n.right, 2*i+2))
            if not _layer:
                return
            nonlocal res
            res = max(res, _layer[-1][1] - _layer[0][1] + 1)
            dfs(_layer)
        dfs([(root, 0)])
        return res
            
    # 322: https://leetcode.cn/problems/coin-change/description/
    def test(self):
        coins = [1, 2, 5]
        amount = 11
        res = 3
        
        # coins = [2]
        # amount = 3
        # res = -1
        
        # coins = [1]
        # amount = 0
        # res = 0
        
        r = self.coinChange(coins, amount)
        print(r)
        print(r == res)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        for i in range(1, amount + 1):
            dp_i = None
            for c in coins:
                a = i - c
                if a < 0:
                    continue
                if a not in dp:
                    continue
                if dp_i == None:
                    dp_i = dp[a] + 1
                else:
                    dp_i = min(dp_i, dp[a]+1)
            if dp_i != None:
                dp[i] = dp_i
        res = dp.get(amount, -1)
        return res
            

if __name__ == '__main__':
    Solution().test()