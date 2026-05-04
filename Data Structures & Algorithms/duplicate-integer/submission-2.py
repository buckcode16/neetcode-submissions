class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        # Hash set uses extra memory, access O(1)
        hs = set()

        for n in nums:

            if n in hs:
                return True
            hs.add(n)

        return False

        