class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            x = 1
            temp_arr = nums[:i] + nums[i+1:]
            
            for j in temp_arr:
                x*=j
            
            res.append(x)
        
        return res