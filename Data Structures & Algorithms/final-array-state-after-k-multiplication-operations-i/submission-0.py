import heapq as hq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[:]

        minHeap = [(n, i) for i, n in enumerate(nums)]

        hq.heapify(minHeap)

        for _ in range(k):
            val, index = hq.heappop(minHeap)
            res[index] *= multiplier
            hq.heappush(minHeap,(res[index],index))

        
        return res