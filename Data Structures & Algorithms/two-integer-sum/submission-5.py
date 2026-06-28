class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in h.keys():
                return [h[diff], i]
            h[nums[i]] = i

        return [0]