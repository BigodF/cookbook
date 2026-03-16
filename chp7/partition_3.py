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
    # 53: https://leetcode.cn/problems/maximum-subarray/
    def maxSubArray_test(self, ):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        res = 6
        
        r = self.maxSubArray(nums)
        print(r)
        print(r==res)
        return
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        last_s = nums[0]
        res = last_s
        for i in range(1, n):
            s = max(last_s, 0) + nums[i]
            res = max(res, s)
            last_s = s
        return res
    
    # 4: https://leetcode.cn/problems/median-of-two-sorted-arrays/
    def test(self, ):
        nums1 = [1,3]
        nums2 = [2]
        res = 2
        
        # nums1 = [1,2]
        # nums2 = [3,4]
        # res = 2.5
        
        nums1 = [2,3,4]
        nums2 = [1]
        res = 2.5
        
        r = self.findMedianSortedArrays(nums1, nums2)
        print(r)
        print(r==res)
        return
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        def find_k(k):
            l0, l1 = 0, 0
            while k > 0:
                if l0 >= m:
                    return nums2[l1 + k - 1]
                if l1 >= n:
                    return nums1[l0 + k - 1]
                if k == 1:
                    if nums1[l0] <= nums2[l1]:
                        return nums1[l0]
                    else:
                        return nums2[l1]
                else:
                    _k = k // 2
                    if m-l0 <= n-l1:
                        l0_com_num = min(m-l0, _k)
                        l1_com_num = k - l0_com_num
                    else:
                        l1_com_num = min(n-l1, _k)
                        l0_com_num = k - l1_com_num
                    _l0 = l0 + l0_com_num - 1
                    _l1 = l1 + l1_com_num - 1
                    if nums1[_l0] <= nums2[_l1]:
                        l0 = _l0 + 1
                        k -= l0_com_num
                    else:
                        l1 = _l1 + 1
                        k -= l1_com_num
        k = (m + n) // 2
        res = find_k(k+1)
        if (m + n) % 2 == 0:
            res = (res + find_k(k)) / 2
        return res

    # 169: https://leetcode.cn/problems/majority-element/description/
    def majorityElement(self, nums: List[int]) -> int:
        '''正确性证明，令众数为x：
        1. 消去部分后，x仍然是剩余部分的众数：
            - 如果cand = x，由于消去的x、非x个数相同，所以x仍然是剩余部分的众数。
            - 如果cand != x，此时消去的x的个数 <= 消去总数的一半，所以x仍然是剩余部分的众数。
        2. 如果cand != x，必然会发生消去。开始cnt=1，由于cand != x，最终的cnt必然<0，所以中间存在=0的位置。
        3. 综上最终的cand一定是x。
        '''
        
        cnt = 0
        cand = None
        for i in nums:
            if cnt == 0:
                cand = i 
            if i == cand:
                cnt += 1
            else:
                cnt -= 1
        return cand
                    
                    
            
            
            

if __name__ == '__main__':
    Solution().test()