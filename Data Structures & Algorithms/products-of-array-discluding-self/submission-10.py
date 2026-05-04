class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = [1] * len(nums)
        
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        # [1,1,2,8]


        post = 1
        # [6,4,2,1]
        # [8,2,1,1] 
        for i in range(len(nums)-1, -1, -1):
            res[i]*=post
            post*=nums[i]
            
        return res