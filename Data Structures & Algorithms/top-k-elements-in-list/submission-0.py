class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        res = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        output = list()

        for i in range(k):
            output.append(res[i])
        
        return output