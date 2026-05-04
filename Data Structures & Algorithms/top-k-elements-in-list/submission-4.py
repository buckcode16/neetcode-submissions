class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for n in nums:
            hm[n] = hm.get(n,0)+1

        count = 0
        res = []
        for key,v in sorted(hm.items(),key = lambda item:item[1], reverse=True):
            res.append(key)
            count+=1
            if count == k:
                return res