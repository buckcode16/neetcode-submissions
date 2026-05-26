class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)

        res = 0

        for n in snums:
            cnt = 0

            if n-1 not in snums:
                while n in snums:
                    cnt+=1
                    n+=1

                res = max(res,cnt)


        return res