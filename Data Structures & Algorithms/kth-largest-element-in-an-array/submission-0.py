import heapq as hp
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        hp.heapify(h)

        for n in nums:
            hp.heappush(h,n)

            if len(h)>k:
                hp.heappop(h)
        return h[0]