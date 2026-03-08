from typing import List
from functools import cmp_to_key

class Solution:
    def threeSum_test(self, ):
        nums = [-1,0,1,2,-1,-4]
        res = [[-1,-1,2],[-1,0,1]]

        # nums = [0,0,0]
        # res = [[0, 0, 0]]

        # nums = [-100,-70,-60,110,120,130,160]
        # res = [[-100,-60,160],[-70,-60,130]]
        
        r = self.threeSum(nums)
        print(r)
        print(r==res)
        return

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        n = len(nums)
        res = []
        for i in range(n):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                while j < k and (j!=i+1 and  nums[j-1] == nums[j]):
                    j += 1
                k0 = 0 - (nums[i] + nums[j])
                while j < k and ((k!=n-1 and nums[k] == nums[k+1]) or nums[k] > k0):
                    k -= 1
                if j < k and nums[k] == k0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                j += 1
        return res
    
    def moveZeroes_test(self, ):
        nums = [0,1,0,3,12]
        res = [1,3,12,0,0]

        # nums = [1, 0]
        # res = [1, 0]

        self.moveZeroes(nums)
        print(nums)
        print(nums==res)
        return
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        n = len(nums)
        while r < n:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        print(l, r)

    def merge_test(self, ):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        res = [1,2,2,3,5,6]

        # nums1 = [1]
        # m = 1
        # nums2 = []
        # n = 0
        # res = [1]

        # nums1 = [0]
        # m = 0
        # nums2 = [1]
        # n = 1
        # res = [1]


        # nums = [1, 0]
        # res = [1, 0]

        self.merge(nums1, m, nums2, n)
        print(nums1)
        print(nums1==res)
        return
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = m + n - 1
        r0, r1 = m - 1, n - 1
        while True:
            while r0 >= 0 and (r1 < 0 or nums1[r0] >= nums2[r1]):
                nums1[r], nums1[r0] = nums1[r0], nums1[r]
                r0 -= 1
                r -= 1
            while r1 >= 0 and (r0 < 0 or nums1[r0] < nums2[r1]):
                nums1[r], nums2[r1] = nums2[r1], nums1[r]
                r1 -= 1
                r -= 1
            if r1 < 0 and r0 < 0:
                break
    
    def test(self, ):
        num1 = "11"
        num2 = "123"
        res = "134"

        num1 = "456"
        num2 = "77"
        res = '533'

        r = self.addStrings(num1, num2)
        print(r)
        print(r==res)
        return
    
    def addStrings(self, num1: str, num2: str) -> str:
        r = max(len(num1), len(num2))
        t = 0
        res = ''
        for i in range(-1, -r-1, -1):
            a = 0 if -i > len(num1) else int(num1[i])
            b = 0 if -i > len(num2) else int(num2[i])
            c = a + b + t
            if c > 9:
                c -= 10
                t = 1
            else:
                t = 0
            res = str(c) + res
        if t:
            res = str(t) + res
        return res
        

        

if __name__ == '__main__':
    Solution().test()