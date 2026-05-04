class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]

        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=post

            # res[3] = 8*1
            # res[2] = 2*6
            # res[1] = 1*24
            # res[0] = 1*48
            post*=nums[i]

            # post = 1*6
            # post = 6*4
            # post = 24*2
            # post = 48*1


        return res