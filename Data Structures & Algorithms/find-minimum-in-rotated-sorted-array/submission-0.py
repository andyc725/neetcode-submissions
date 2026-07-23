class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if r - l == nums[r] - nums[l]:
            return nums[l]
        res = 0
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] - nums[l] < 0:
                r = mid
                res = mid
            elif nums[r] - nums[mid] < 0:
                l = mid + 1
                res = r
            else:
                return nums[l]
        return nums[res]
            
