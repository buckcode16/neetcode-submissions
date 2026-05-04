class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_bkt = [[] for i in range(len(nums)+1)]
        count = {}

        for n in nums:
            count[n]=1 + count.get(n,0)

        for key,value in count.items():
            freq_bkt[value].append(key)

        res = []
        for i in range(len(freq_bkt)-1,0,-1):
            for num in freq_bkt[i]:
                res.append(num)
                if len(res) == k:
                    return res 