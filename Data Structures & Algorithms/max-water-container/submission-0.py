class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = 0
        while l < r:
            A = (r - l) * min(heights[l], heights[r])
            if A > maxA:
                maxA = A
            
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
        
        return maxA