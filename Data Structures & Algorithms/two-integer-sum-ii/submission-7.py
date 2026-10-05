class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        get = {}
        for i in range(len(numbers)):
            if target - numbers[i] not in get:
                get[numbers[i]] = i
            else:
                return [get[target - numbers[i]] + 1, i + 1]
        return [0, 0]