class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n]+=1

        # frequent_keys = [key for key, value in hashmap.items() if value >= k]
        buckets = []

        for _ in range(len(nums) + 1):
            buckets.append([])
        
        for key, v in hashmap.items():
            buckets[v].append(key)

        top_k = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                top_k.append(j)
        
                if len(top_k) == k:
                    return top_k
        return top_k
