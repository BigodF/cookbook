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
            
    def test(self, ):
        # nums = [1,2,3,1]
        # res = [2]
        
        nums = [1,2,1,3,5,6,4]
        res = [1, 5] 
        
        r = self.findPeakElement(nums)
        print(r)
        print(r in res)
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
                    

if __name__ == '__main__':
    Solution().test()