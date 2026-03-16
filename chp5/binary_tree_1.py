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
            _layers = [nodes[i+st] for i in range(2*len(layers))]
            for i, node in enumerate(layers):
                node.left = _layers[2*i]
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
    # 144: https://leetcode.cn/problems/binary-tree-preorder-traversal/
    def Traversal_test(self, ):
        root = [3,9,20,None,None,15,7]
        res = [[3],[9,20],[15,7]]
        res = [[3],[20,9],[15,7]]
        
        root = [1,2,3,4,None,None,5]
        res = [[1],[3,2],[4,5]]
        
        root = list2Tree(root)
        r = self.Traversal(root)
        print(r)
        print(r==res)
        return
    def Traversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preorderTraversal(root: Optional[TreeNode]):
            if not root:
                return
            res.append(root.val)
            preorderTraversal(root.left)
            preorderTraversal(root.right)
        # preorderTraversal(root)
        
        def inorderTraversal(root: Optional[TreeNode]):
            if not root:
                return
            inorderTraversal(root.left)
            res.append(root.val)
            inorderTraversal(root.right)
        # inorderTraversal(root)
        
        def levelOrder(nodes: List[TreeNode]):
            tmp = []
            _res = []
            for n in nodes:
                if not n:
                    continue
                _res.append(n.val)
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            if _res:
                res.append(_res)
            if tmp:
                levelOrder(tmp)
        # levelOrder([root])
        
        def zigzagLevelOrder(nodes: List[Optional[TreeNode]], reverse=False):
            tmp = []
            _res = [n.val for n in nodes if n]
            if not _res:
                return
            if reverse:
                _res = _res[::-1]
            res.append(_res)
            for n in nodes:
                if not n:
                    continue
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            if tmp:
                zigzagLevelOrder(tmp, reverse=not reverse)
        zigzagLevelOrder([root])
        return res
            
    # 236: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/
    def lowestCommonAncestor_test(self, ):
        root = [3,5,1,6,2,0,8,None,None,7,4]
        p = 5
        q = 4
        res = 5
        
        # root = [1,2,3,4,None,None,5]
        # res = [[1],[3,2],[4,5]]
        
        root, node_list = list2Tree(root)
        for n in node_list:
            if not n: continue
            if n.val == p:
                p = n
            if n.val == q:
                q = n
            if n.val == res:
                res = n
        r = self.lowestCommonAncestor(root, p, q)
        print(r)
        print(r==res)
        return
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: TreeNode):
            if not root:
                return False, False, None
            find_p = False
            find_q = False
            if root == p:
                find_p = True
            elif root == q:
                find_q = True
            l_find_p, l_find_q, l_node = dfs(root.left)
            if l_find_p and l_find_q:
                return l_find_p, l_find_q, l_node
            r_find_p, r_find_q, r_node = dfs(root.right)
            if r_find_p and r_find_q:
                return r_find_p, r_find_q, r_node
            fp = find_p or l_find_p or r_find_p
            fq = find_q or l_find_q or r_find_q
            if fp and fq:
                return fp, fq, root
            else:
                return fp, fq, None
        return dfs(root)[-1]
    
    # 112: https://leetcode.cn/problems/path-sum/
    def pathSum_test(self, ):
        root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
        targetSum = 22
        res = [[5,4,11,2],[5,8,4,5]]
        
        # root = [1,2,3]
        # targetSum = 5
        # res = False
        
        # root = []
        # targetSum = 0
        # res = False
        
        # root = [1,2,3,4,None,None,5]
        # res = [[1],[3,2],[4,5]]
        
        root, node_list = list2Tree(root)
        r = self.pathSum(root, targetSum)
        # print(r)
        assert len(r) == len(res)
        for _r, _res in zip(r, res):
            # _r = [n.val for n in _r]
            assert(_r==_res)
        return
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum):
            if not root:
                return []
            if root.left == None and root.right == None:
                if targetSum == root.val:
                    return [[root.val]]
                else:
                    return []
            targetSum -= root.val
            res = []
            res.extend(dfs(root.left, targetSum))
            res.extend(dfs(root.right, targetSum))
            for r in res:
                r.insert(0, root.val)
            return res
        res = dfs(root, targetSum)
        return res 
    
    # 101: https://leetcode.cn/problems/symmetric-tree/
    def isSymmetric_test(self, ):
        root = [1,2,2,3,4,4,3]
        res = True
        
        root = [1,2,2,None,3,None,3]
        res = False
        
        root, node_list = list2Tree(root)
        r = self.isSymmetric(root)
        print(r)
        print(r==res)
        return
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(layer):
            _layer = []
            for n in layer:
                _layer.append(n.left)
                _layer.append(n.right)
            l, r = 0, len(_layer) - 1
            while l < r:
                ln = _layer[l]
                rn = _layer[r]
                if (ln==None and rn!=None) or (ln!=None and rn==None) or (ln!=None and rn!=None and ln.val!=rn.val):
                    return False
                l += 1
                r -= 1
            _layer = [t for t in _layer if t]
            if _layer:
                return dfs(_layer)
            else:
                return True
        return dfs([root])
    
    # 124: https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
    def maxPathSum_test(self, ):
        root = [1,2,3]
        res = 6
        
        # root = [-10,9,20,None,None,15,7]
        # res = 42
        
        root, node_list = list2Tree(root)
        r = self.maxPathSum(root)
        print(r)
        print(r==res)
        return
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res: int = None
        def dfs(root):
            # 返回经过root的最大路径和
            nonlocal res
            if not root:
                return 0
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            child_max = max(left_max, right_max)
            # root_max不包括同时包含左右子节点的情况，因为同时包含左右子节点时，root为最高节点，路径不能再往上，但这种情况也算在路径。
            # root_max表示可以路径可以继续往上的情况，分为三种情况，root单独，root和左，root和右。
            root_max = root.val
            if child_max > 0:
                root_max += child_max
            # 更新结果，需要考虑四种情况，以上三种，加上root为最高节点的情况（同时包含左子节点、root、右子节点）
            if res == None:
                res = max(root_max, left_max + right_max + root.val)
            else:
                res = max(res, root_max, left_max + right_max + root.val)
            return root_max
        dfs(root)
        return res
    
    # 105： https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    def buildTree_test(self, ):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        res = [3,9,20,None,None,15,7]
        
        preorder = [-1]
        inorder = [-1]
        res = [-1]
        
        # root = [-10,9,20,None,None,15,7]
        # res = 42
        
        res_tree, node_list = list2Tree(res)
        r = self.buildTree(preorder, inorder)
        r_list = Tree2list(r)
        print(r_list)
        print(res == r_list)
        return
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n2idx = {n:i for i, n in enumerate(inorder)}
        def dfs(pl, pr, il, ir):
            if pl > pr:
                return None
            n = TreeNode(preorder[pl])
            idx = n2idx[preorder[pl]]
            left_num = idx - il
            n.left = dfs(pl+1, pl+left_num, il, idx-1)
            n.right = dfs(pl+left_num+1, pr, idx+1, ir)
            return n
        root = dfs(0, len(preorder)-1, 0, len(inorder)-1)
        return root
    
    # 98: https://leetcode.cn/problems/validate-binary-search-tree/description/
    def test(self, ):
        root = [2,1,3]
        res = True
        
        root = [5,1,4,None,None,3,6]
        res = False
        
        # root = [-10,9,20,None,None,15,7]
        # res = 42
        
        root, node_list = list2Tree(root)
        r = self.isValidBST(root)
        # r_list = Tree2list(r)
        print(r)
        print(res == r)
        return
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_v, max_v):
            if min_v != None and root.val <= min_v:
                return False
            if max_v != None and root.val >= max_v:
                return False
            if root.left:
                left_max = root.val if max_v == None else min(root.val, max_v)
                left_ret = dfs(root.left, min_v, left_max)
                if not left_ret:
                    return False
            if root.right:
                right_min = root.val if min_v==None else max(root.val, min_v)
                right_ret = dfs(root.right, right_min, max_v)
                if not right_ret:
                    return False
            return True
        return dfs(root, None, None)
    
    # 110: https://leetcode.cn/problems/balanced-binary-tree/
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root == None:
                return 0
            left_deep = dfs(root.left)
            right_deep = dfs(root.right)
            if left_deep < 0 or right_deep < 0 or abs(left_deep-right_deep) > 1:
                return -1
            else:
                return max(left_deep, right_deep)+1
        res = dfs(root)
        return res >= 0
        
        

if __name__ == '__main__':
    Solution().test()