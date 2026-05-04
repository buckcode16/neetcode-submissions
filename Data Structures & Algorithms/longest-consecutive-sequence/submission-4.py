class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        longest = 0

        for n in set_nums:
            temp_count = 0
            if n-1 not in set_nums:
                while n in set_nums:
                    temp_count+=1
                    n+=1
                
            longest = max(longest, temp_count)

        return longest