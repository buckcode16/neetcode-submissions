class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i],0)+1

            if freq_map.get(nums[i]) > 1:
                return True
        
        return False