class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix postfix

        pre = []
        m = 1
        for n in nums:
            m*=n

            pre.append(m)

        post = []
        m = 1
        for n in nums[::-1]:
            m*=n

            post.append(m)

        post = post[::-1]

        res = [0] * len(nums)

        for n in range(len(nums)):
            if n == 0:
                res[n] = post[n+1]
                continue
            if n == len(nums)-1:
                res[n] = pre[n-1]
                continue
            
            res[n] = pre[n-1]*post[n+1]
            
        return res