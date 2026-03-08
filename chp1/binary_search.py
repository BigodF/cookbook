from typing import List
from functools import cmp_to_key

class Solution:
    def search_test(self, ):
        nums = [-1,0,3,5,9,12]
        target = 9
        res = 4
        
        nums = [-1,0,3,5,9,12]
        target = 2
        res = -1
        
        r = self.search(nums, target)
        print(r)
        print(r==res)
        return
        
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if l < len(nums) and nums[l] == target:
            return l
        return -1
    
    def searchRange_test(self, ):
        nums = [5,7,7,8,8,10]
        target = 8
        res = [3, 4]
        
        # nums = [5,7,7,8,8,10]
        # target = 6
        # res = [-1, -1]
        
        nums = [1]
        target = 1
        res = [0, 0]
        
        r = self.searchRange(nums, target)
        print(r)
        print(r==res)
        return
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def _search(include_eq=False):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if (not include_eq and nums[m] < target) or (include_eq and nums[m] <= target):
                    l = m + 1
                else:
                    r = m
            if include_eq:
                l -= 1
            if 0 <= l < len(nums) and nums[l] == target:
                return l
            return -1
        return [_search(), _search(include_eq=True)]
    
    def findMin_test(self, ):
        nums = [3,4,5,1,2]
        res = 1
        
        # nums = [11,13,15,17]
        # res = 11
        
        nums = [4,5,6,7,0,1,2]
        res = 0
        
        nums = [2, 1]
        res = 1
        
        r = self.findMin(nums)
        print(r)
        print(r==res)
        return
    
    def findMin(self, nums: List[int]) -> int:
        # if nums[0] <= nums[-1]:
        #     return nums[0]
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m
        if l < len(nums):
            return nums[l]
        return nums[0]

    
    def rotate_search_test(self, ):
        nums = [4,5,6,7,0,1,2]
        target = 0
        res = 4
        
        # nums = [4,5,6,7,0,1,2]
        # target = 3
        # res = -1
        
        # nums = [1]
        # target = 0
        # res = -1
        
        nums = [1, 3]
        target = 1
        res = 0
        
        r = self.rotate_search(nums, target)
        print(r)
        print(r==res)
        return
    
    def rotate_search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        left_flag = True
        if target < nums[0]:
            left_flag = False
            
        while l < r:
            m = (l + r) // 2
            if left_flag:
                if nums[m] < nums[0]:
                    r = m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m
            else:
                if nums[m] >= nums[0] or nums[m] < target:
                    l = m + 1
                else:
                    r = m
        if l < len(nums) and nums[l] == target:
            return l
        return -1
            
    def findPeakElement_test(self, ):
        # nums = [1,2,3,1]
        # res = [2]
        
        nums = [1,2,1,3,5,6,4]
        res = [1, 5] 
        
        r = self.findPeakElement(nums)
        print(r)
        print(r in res)
        s = '''
背景：在搜索热点流下推荐用户感兴趣的微博，提升用户消费。
工作：完成从LR到深度模型的升级，使用EasyRec(TensorFlow)训练框架，在DLRM模型的基础上进行升级，提升符合用户兴趣的微博排序。训练样本通过样本标签、样本权重、用户兴趣构造pairwise的训练数据；模型结构上，增加pair label tower，与ctr tower共享底层参数，线上预测采用两个塔概率乘积排序；通过这种方式让更符合用户兴趣的样本排序更高。线上服务采用tfserving，使用预热的方式，解决更新模型文件的延迟问题。最终离线auc提升0.32，top@10的用户兴趣博文占比由12.9%提升15.8%，相对提升22.4%，线上用户消费条数提升11.3%。

背景：构建种草微博库，满足用户在搜索时，对旅游、美妆、数码等类目的攻略需求。
工作：使用MMBT多模态模型做分类任务，构建入库筛选流程。图片使用resnet编码，和文本embedding concat后输入到roberta；为了去除标注数据中的噪声，在二分类主任务之外添加了两个辅助任务：8分类的领域分类任务、对比学习。对比学习是在pooling之后的embedding后，经过mlp映射到128维向量表示，在batch内两两结合做对比学习。最终分类准确率达到95%，相比base版本79%，相对提升20.2%。

'''

        return
    
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def getm(i):
            if i < 0 or i >= n:
                return (0, 0)
            return (1, nums[i])
                
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if getm(m-1) < getm(m) and getm(m) > getm(m+1):
                return m
            if getm(m-1) < getm(m):
                l = m + 1
            else:
                r = m
        return l
    
    def findCircleNum_test(self, ):
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        res = 2
        
        # isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        # res = 3
        
        r = self.findCircleNum(isConnected)
        print(r)
        print(r == res)
        return
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        label = [-1] * n
        set_idx = 0
        def dfs(i, set_idx):
            for j in range(n):
                if isConnected[i][j] == 1 and label[j] == -1:
                    label[j] = set_idx
                    dfs(j, set_idx)
        for i in range(n):
            if label[i] == -1:
                dfs(i, set_idx)
                set_idx += 1
        return set_idx

    def findMedianSortedArrays_test(self, ):
        nums1 = [1,3]
        nums2 = [2]
        res = 2
        
        # nums1 = [1,2]
        # nums2 = [3,4]
        # res = 2.5

        # nums1 = [2, 3, 4]
        # nums2 = [1]
        # res = 2.5

        # nums1 = [2,3,4,5,6]
        # nums2 = [1]
        # res = 3.5
        
        
        
        r = self.findMedianSortedArrays(nums1, nums2)
        print(r)
        print(r == res)
        return

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def dfs(l0, r0, l1, r1, k):
            if l0 >= r0:
                return nums2[l1 + k-1]
            elif l1 >= r1:
                return nums1[l0 + k-1]
            
            if k == 1:
                return min(nums1[l0], nums2[l1])
            elif k == 2:
                if nums1[l0] < nums2[l1]:
                    return dfs(l0+1, r0, l1, r1, k-1)
                else:
                    return dfs(l0, r0, l1+1, r1, k-1)
                
            km = (k - 1) // 2
            if r0 - l0 < r1 - l1:
                m0 = min(r0 - l0, km)
                m1 = k - 1 - m0
            else:
                m1 = min(r1 - l1, km)
                m0 = k - 1 - m1

            
            if nums1[l0 + m0-1] < nums2[l1 + m1-1]:
                return dfs(l0 + m0, r0, l1, r1, k-m0)
            else:
                return dfs(l0, r0, l1+m1, r1, k-m1)

        n0, n1 = len(nums1), len(nums2)
        k = (n0 + n1) // 2
        res = dfs(0, len(nums1), 0, len(nums2), k+1)
        if (n0 + n1) % 2 == 0:
            b = dfs(0, len(nums1), 0, len(nums2), k)
            res = (res + b) / 2
        return res
    
    def searchMatrix_test(self, ):
        matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        target = 5
        res = True
        
        matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        target = 20
        res = False
        
        r = self.searchMatrix(matrix, target)
        print(r)
        print(r == res)
        return
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
    
    def test(self):
        x = 4
        res = 2

        # x = 8
        # res = 2

        r = self.mySqrt(x)
        print(r)
        print(r == res)
        return

    def mySqrt(self, x: int) -> int:
        l, r = 0, x + 1
        while l < r:
            m = (l + r) // 2
            if m * m < x:
                l = m + 1
            else:
                r = m
        if l * l > x:
            l -= 1
        return l


if __name__ == '__main__':
    Solution().test()