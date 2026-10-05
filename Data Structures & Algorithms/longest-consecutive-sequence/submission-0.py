class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        length = 1

        for n in nums:
            if n - 1 not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
            '''else:
                while n - 1 in numSet:
                    n -= 1
                    length += 1
            '''
            longest = max(length, longest)

        return longest