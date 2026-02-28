from typing import List
from functools import cmp_to_key

class Solution:
    def sortArray_test(self):
        nums = [5,2,3,1]
        res = sorted(nums)
        r = self.sortArray_quick(nums)
        print(r)
        print(r==res)
        return
    
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergesort(l, m)
            mergesort(m+1, r)
            tmp = []
            l1 = l
            l2 = m+1
            while len(tmp) < r - l + 1:
                while l1 <= m and (l2 > r or nums[l1] < nums[l2]):
                    tmp.append(nums[l1])
                    l1 += 1
                while l2 <= r and (l1 > m or nums[l2] <= nums[l1]):
                    tmp.append(nums[l2])
                    l2 += 1
            nums[l:r+1] = tmp
        mergesort(0, len(nums)-1)
        return nums

    def sortArray_quick(self, nums: List[int]) -> List[int]:
        def quicksort(l, r):
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
            nums[r], nums[l0] = nums[l0], nums[r]
            quicksort(l0, r-1)
            quicksort(r+1, r0)
        quicksort(0, len(nums)-1)
        return nums
    
    def findKthLargest_test(self):
        nums = [3,2,1,5,6,4]
        k = 2
        res = 5
        # nums = [3,2,3,1,2,4,5,5,6]
        # k = 4
        # res = 4
        
        r = self.findKthLargest(nums=nums, k=k)
        print(r)
        print(r==res)
        return
    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxheapify(nums, i, heapsize):
            l = 2*i + 1
            r = l+1
            largest_idx = i
            if l < heapsize and nums[l] > nums[largest_idx]:
                largest_idx = l
            if r < heapsize and nums[r] > nums[largest_idx]:
                largest_idx = r
            if largest_idx != i:
                nums[largest_idx], nums[i] = nums[i], nums[largest_idx]
                maxheapify(nums, largest_idx, heapsize)
        heapsize = len(nums)
        for i in range(heapsize-1, -1, -1):
            maxheapify(nums, i, heapsize)
        
        for i in range(k-1):
            nums[0], nums[heapsize-1] = nums[heapsize-1], nums[0]
            heapsize -= 1
            maxheapify(nums, 0, heapsize)

        return nums[0]
    
    def merge_test(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        res = [1,2,2,3,5,6]
        
        # nums = [3,2,3,1,2,4,5,5,6]
        # k = 4
        # res = 4
        
        self.merge(nums1, m, nums2, n)
        print(nums1)
        print(nums1==res)
        return
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        l0, l1 = 0, 0
        while True:
            while l0 < m and (l1 >= n or nums1[l0] <= nums2[l1]):
                tmp.append(nums1[l0])
                l0 += 1
            while l1 < n and (l0 >= m or nums1[l0] > nums2[l1]):
                tmp.append(nums2[l1])
                l1 += 1
            if l0 >= m and l1 >= n:
                break
        nums1[:] = tmp[:]
    
    def majorityElement_test(self):
        nums1 = [2, 1, 2]
        res = 2
        
        # nums = [3,2,3,1,2,4,5,5,6]
        # k = 4
        # res = 4
        
        r = self.majorityElement(nums1)
        print(r)
        print(r==res)
        return
    
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        cand = nums[0]
        for i in nums:
            if cnt == 0:
                cand = i 
            if i == cand:
                cnt += 1
            else:
                cnt -= 1
        return cand
    
    def singleNumber_test(self):
        nums1 = [2, 1, 2, 1, 3]
        res = 1
        
        # nums = [3,2,3,1,2,4,5,5,6]
        # k = 4
        # res = 4
        
        r = self.singleNumber(nums1)
        print(r)
        print(r==res)
        return
    
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for t in nums[1:]:
            res ^= t
        return res
    
    def merge_test(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        res = [[1,6],[8,10],[15,18]]
        
        # intervals = [[1,4],[4,5]]
        # res = [[1, 5]]
        
        r = self.merge(intervals)
        print(r)
        print(r==res)
        return
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        l, r = None, None
        for _l, _r in intervals:
            if l == None:
                l, r = _l, _r
            else:
                if r >= _r:
                    continue
                elif r >= _l:
                    r = _r
                else:
                    res.append([l, r])
                    l, r = _l, _r
        if l != None:
            res.append([l, r])
        return res
    
    def test(self):
        nums = [10,2]
        res = '210'
        
        # nums = [3,30,34,5,9]
        # nums.sort(key=lambda x: str(x))
        # res = '9534330'
        
        r = self.largestNumber(nums)
        print(r)
        print(r==res)
        return
    
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            return  int(b + a) - int(a + b)
            if int(a + b) >= int(b + a):
                return 1
            else:
                return 0
        nums: List[str] = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(cmp))
        if nums[0] == '0':
            return '0'
        return ''.join(nums)

if __name__ == '__main__':
    Solution().test()