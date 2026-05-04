class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            complement = target - value
            
            if complement in hashmap:
                # if hashmap[value] != hashmap[complement]:
                return [hashmap[complement],index]
                
            hashmap[value] = index