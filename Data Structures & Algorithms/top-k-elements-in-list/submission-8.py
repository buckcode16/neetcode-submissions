class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        maxHeap = [[-cnt, x] for x, cnt in count.items()]
        heapq.heapify(maxHeap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])


        return res