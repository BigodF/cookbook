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
    # 78: https://leetcode.cn/problems/subsets/
    def subsets_test(self):
        nums = [1,2,3]
        res = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        
        nums = [0]
        res = [[], [0]]
        
        r = self.subsets(nums)
        print(r)
        print(r == res)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                r = [c for c in res[j]]
                r.append(nums[i])
                res.append(r)
        return res
    
    # 221: https://leetcode.cn/problems/maximal-square/description/
    def maximalSquare_test(self):
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        res = 4
        
        matrix = [["0","1"],["1","0"]]
        res = 1
        
        matrix = [["0"]]
        res = 0
        
        r = self.maximalSquare(matrix)
        print(r)
        print(r == res)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0:
                    continue
                if i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                res = max(res, matrix[i][j]*matrix[i][j])
        return res
    
    # 1277: https://leetcode.cn/problems/count-square-submatrices-with-all-ones/description/
    def countSquares_test(self, ):
        matrix =[
            [0,1,1,1],
            [1,1,1,1],
            [0,1,1,1]
        ]
        res = 15
        
        # matrix = [
        #     [1,0,1],
        #     [1,1,0],
        #     [1,1,0]
        # ]
        # res = 7
        
        r = self.countSquares(matrix)
        print(r)
        print(r == res)
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''dp表示以(i, j)为右下角的正方形的最大边长。
        更新规则（matrix[i, j]==1下，=0时不可做正方形）：
        1. 可以通过作图证明，
            dp[i, j] <= dp[i-1, j] + 1
            dp[i, j] <= dp[i, j-1] + 1
            dp[i, j] <= dp[i-1, j-1] + 1
            联立可得: dp[i, j] <= min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1]) + 1
        2. 分别以(i-1, j)、(i, j-1)、(i-1, j-1)为右下角，以min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1])为边长做图，可以发现能做出(i, j)为右下角，min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1])+1为边长的正方形，也就是说
            dp[i, j] >= min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1]) + 1
        3. 由1、2可得，dp[i, j] = min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1]) + 1
        '''
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                c = None
                for x, y in ((i-1, j), (i, j-1), (i-1, j-1)):
                    if 0 <= x and 0 <= y:
                        if c == None:
                            c = matrix[x][y]
                        else:
                            c = min(c, matrix[x][y])
                    else:
                        c = 0
                        break
                if c != None:
                    matrix[i][j] = c + 1
                res += matrix[i][j]
        return res
    
    
    # 24: https://leetcode.cn/problems/swap-nodes-in-pairs/
    def test(self, ):
        head = [1,2,3,4]
        res = [2,1,4,3]
        
        # head = []
        # res = []
        
        # head = [1]
        # res = [1]
        
        head, node_list = list2linked_list(head)
        r = self.swapPairs(head)
        r_list = linked_list2list(r)
        print(r_list)
        print(res == r_list)
        return
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        last = None
        while tmp and tmp.next:
            x = tmp
            y = tmp.next
            next_node = y.next
            if last:
                last.next = y
            else:
                head = y
            last = x
            y.next = x
            x.next = next_node
            tmp = next_node
        return head
    
    # 92: https://leetcode.cn/problems/reverse-linked-list-ii/description/
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        
        cur = dummy_node
        pre = None
        for _ in range(left):
            pre = cur
            cur = cur.next
        
        reverse_tail = cur
        cur = cur.next
        for _ in range(right-left):
            reverse_head = pre.next
            pre.next = cur
            reverse_tail.next = cur.next
            cur.next = reverse_head
            cur = reverse_tail.next
        return dummy_node.next
    
    # 70: https://leetcode.cn/problems/climbing-stairs/
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
            
    
        
if __name__ == '__main__':
    Solution().test()