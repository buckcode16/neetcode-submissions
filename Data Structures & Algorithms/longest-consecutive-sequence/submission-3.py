class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for n in set_nums:
            if (n - 1) not in set_nums:
                
                current_streak = 1

                while (n + 1) in set_nums:
                    n += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest