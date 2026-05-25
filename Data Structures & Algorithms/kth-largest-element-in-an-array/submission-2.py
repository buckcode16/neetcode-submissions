class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]

        heapq.heapify(maxHeap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxHeap))


        return -res[-1]