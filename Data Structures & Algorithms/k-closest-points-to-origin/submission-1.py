class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [[math.sqrt(x[0]**2 + x[1]**2), x] for x in points]

        heapq.heapify(maxHeap)
        
        res = []

        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res