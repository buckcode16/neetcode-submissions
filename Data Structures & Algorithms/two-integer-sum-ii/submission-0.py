class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        hm = {}

        for i, n in enumerate(numbers, start=1):
            complement = target - n

            if complement in hm:
                return [min(hm[complement],i), max(hm[complement],i)]

            hm[n] = i

        return res