class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, i, b = 0, 0, len(nums) - 1 
        #seen2 = False
        #for i in range(len(nums)):
        while i <= b: 
            if nums[i] == 0:
                nums[i], nums[a] = nums[a], nums[i]
                a += 1
                i += 1
                #b += 1
            elif nums[i] == 1:
                #nums[i], nums[a + 1] = nums[a + 1], nums[i]
                i += 1
            #elif seen2 == False:
            else:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1