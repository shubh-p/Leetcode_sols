class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, m * n - 1  # Adjusted starting and ending indices

        while i <= j:
            mid = (i + j) // 2
            c = mid % n
            r = mid // n  # Adjusted row calculation
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                j = mid - 1
            else:
                i = mid + 1
                
        return False
