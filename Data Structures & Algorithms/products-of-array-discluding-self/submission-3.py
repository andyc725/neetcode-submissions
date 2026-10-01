class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        hasZero = False
        allZero = False
        zeroCount = 0
        zero = set()
        for i in range(len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            else:
                hasZero = True
                zero.add(i)
                zeroCount = 1 + zeroCount

        if zeroCount == len(nums):
            allZero = True
            for i in range(len(nums)):
                res.append(0)
            return res

        if hasZero == False:
            for i in range(len(nums)):
                res.append(int(product / nums[i]))
        else:
            if zeroCount == 1: 
                for i in range(len(nums)):
                    if i in zero:
                        res.append(int(product))
                    else:
                        res.append(0)
            else:
                for i in range(len(nums)):
                    res.append(0)
                            
        return res