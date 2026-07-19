class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1,r1 = 0, len(matrix) - 1
        #l2, r2 = 0, len(matrix[0])

        while l1 <= r1:
            mid1 = l1 + ((r1 - l1) // 2)

            if target in matrix[mid1]:
                return True
            elif matrix[mid1][-1] < target:
                l1 = mid1 + 1
            else:
                r1 = mid1 - 1
        
        return False
