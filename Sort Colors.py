class Solution:
    def sortColors(self, nums: list[int]) -> None:
        self.nums= {
            0:'red',
            1:'white',
            2:'blue'
        }


        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] >= nums[j]:
                    nums[i], nums[j] = nums[j],nums[i]
                    
        return nums
sol=Solution()
result = sol.sortColors([2,0,2,1,1,0])
print(result)
