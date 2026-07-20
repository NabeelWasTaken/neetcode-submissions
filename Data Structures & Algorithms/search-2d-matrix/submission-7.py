class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS - 1

        while l <= r:

            mid = math.floor((l + r) / 2)

            if matrix[mid][0] > target:
                r = mid - 1
            
            elif matrix[mid][COLS - 1] < target:
                l = mid + 1
            
            else:
                break
            
        
        l = 0
        r = COLS - 1

        while l <= r:

            mid2 = (l + r) // 2

            if matrix[mid][mid2] > target:
                r = mid2 - 1
            elif matrix[mid][mid2] < target:
                l = mid2 + 1
            elif matrix[mid][mid2] == target:
                return True
        
        return False





        