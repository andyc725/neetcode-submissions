class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        output = list()
        i, j, k = 0, 1, len(nums) - 1
        for i in range(len(nums)):
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    ans = [nums[i], nums[j], nums[k]]
                    if ans not in output:
                        ans.sort()
                        output.append(ans)
                    
                    j += 1
                    k -= 1
                    
            j = i + 2
            k = len(nums) - 1
        
        return output