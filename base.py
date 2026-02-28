from typing import List
from functools import cmp_to_key

class Solution:
    def test(self, ):
        nums = [-1,0,3,5,9,12]
        target = 9
        res = 4
        
        r = self.search(nums)
        print(r)
        print(r==res)
        return
        
    def search(self, nums: List[int], target: int) -> int:
        return

if __name__ == '__main__':
    Solution().test()