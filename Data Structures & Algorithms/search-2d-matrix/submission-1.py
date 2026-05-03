class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        l = 0
        r = len(matrix) - 1

        n = len(matrix[0]) - 1

        

        while l <= r:
            
            mid = l + (r - l) // 2
            
            if target < matrix[mid][0]:
                r = mid - 1
            
            elif target > matrix[mid][n]:
                l = mid + 1
            else:
                break

        
        l = 0
        r = len(matrix[0]) - 1
        
        while l <= r:
            mid2 = (l + r)//2

            if target > matrix[mid][mid2]:
                l = mid2 + 1
            elif target < matrix[mid][mid2]:
                r = mid2 - 1
            elif target == matrix[mid][mid2]:
                return True
            
        
        return False


        
