import heapq as hq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        hq.heapify(self.h)

        for n in nums:
            hq.heappush(self.h, n)
            if len(self.h) > self.k:
                hq.heappop(self.h)

        


    def add(self, val: int) -> int:
        hq.heappush(self.h,val)

        if len(self.h) > self.k:
            hq.heappop(self.h)
        return self.h[0]
