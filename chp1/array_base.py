from typing import List

class Solution:
    def rotate_array(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0, 25.95
        # l = len(nums)
        # 
        # nums[:] = nums[-k:] + nums[:-k]
        
        
        l = len(nums)
        k = k % l
        cnt = 0
        st = 0
        while cnt < l:
            tmp = nums[st]
            i = (st + k) % l
            while i != st:
                nums[i], tmp = tmp, nums[i]
                i = (i + k) % l
                cnt += 1
            nums[st] = tmp
            cnt += 1
            st += 1
        return
    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        cnt = 0
        x, y = 0, 0
        m, n = len(mat), len(mat[0])
        num = m * n
        right_up = True
        while cnt < num:
            res.append(mat[y][x])
            cnt += 1
            if right_up:
                y -= 1
                x += 1
            else:
                y += 1
                x -= 1
            
            if x < n and y < 0:
                y += 1
                right_up = not right_up
            elif x == n and y < m:
                y += 2
                x -= 1
                right_up = not right_up
            elif x < 0 and 0 <= y < m:
                x += 1
                right_up = not right_up
            elif y >= m:
                x += 2
                y -= 1
                right_up = not right_up
                
        return res
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n % 2 == 0:
            _m = _n = n // 2
        else:
            _m = n // 2
            _n = _m + 1
        for i in range(_m):
            for j in range(_n):
                tmp = matrix[i][j]
                matrix[j][n-1-i], tmp = tmp, matrix[j][n-1-i]
                matrix[n-1-i][n-1-j], tmp = tmp, matrix[n-1-i][n-1-j]
                matrix[n-1-j][i], tmp = tmp, matrix[n-1-j][i]
                matrix[i][j] = tmp
                pass
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        cnt = 0
        m, n = len(matrix), len(matrix[0])
        total_num = m * n
        l, r, u, b = 0, n-1, 0, m-1
        while cnt < total_num:
            if l == r:
                for i in range(u, b+1):
                    res.append(matrix[i][l])
                    cnt += 1
            elif u == b:
                for j in range(l, r+1):
                    res.append(matrix[u][j])
                    cnt +=1
            else:
                for j in range(l, r):
                    res.append(matrix[l][j])
                    cnt += 1
                for i in range(u, b):
                    res.append(matrix[i][r])
                    cnt += 1
                for j in range(r, l, -1):
                    res.append(matrix[b][j])
                    cnt += 1
                for i in range(b, u, -1):
                    res.append(matrix[i][l])
                    cnt += 1
                l += 1
                r -= 1
                u += 1
                b -= 1
        return res
    
    def generateSpiralOrderMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        l, r, t, b = 0, n-1, 0, n-1
        x = 1
        while l <= r and t <= b:
            for j in range(l, r+1):
                res[t][j] = x
                x += 1
            for i in range(t+1, b):
                res[i][r] = x
                x += 1
            if l < r and t < b:
                for j in range(r, l, -1):
                    res[b][j] = x
                    x += 1
                for i in range(b, t, -1):
                    res[i][l] = x
                    x += 1
            l += 1
            r -= 1
            t += 1
            b -= 1
        return res
                
                


        

if __name__ == '__main__':
    s = Solution()
    
    # nums = [1,2,3,4,5,6,7]
    # k = 3
    # # nums, k = [-1,-100,3,99], 2
    # # [-1,-100,3,99]
    # # [3,99,-1,-100]
    # print(nums)
    # s.rotate(nums, k)
    # print(nums)
    
    # mat = [[1,2,3],[4,5,6],[7,8,9]]
    # # mat = [[1,2],[3,4]]
    # res = s.findDiagonalOrder(mat)
    # print(res)
     
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # # [[7,4,1],[8,5,2],[9,6,3]]
    # matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    # s.rotate(matrix)
    # print(matrix)
    
    
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # res = [1,2,3,6,9,8,7,4,5]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # res = [1,2,3,4,8,12,11,10,9,5,6,7]
    # matrix = [[6,9,7]]
    # res = [6, 9, 7]
    # r = s.spiralOrder(matrix)
    
    
    
    n = 1
    res = [[1,2,3],[8,9,4],[7,6,5]]
    r = s.generateSpiralOrderMatrix(n)
    
    
    print(r)
    print(r == res)
    
    