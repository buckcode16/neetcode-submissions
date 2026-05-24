import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [[math.sqrt((x[0]**2+x[1]**2)), x] for x in points]
        res = []
        heapq.heapify(minHeap)
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res