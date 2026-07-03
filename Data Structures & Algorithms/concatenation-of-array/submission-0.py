class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums) * 2):
            if i < len(nums):
                res.append(nums[i])
            else:
                res.append(nums[i - len(nums)])
        
        return res