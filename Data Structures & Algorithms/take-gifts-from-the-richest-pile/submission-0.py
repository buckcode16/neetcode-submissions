import heapq as hq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        inverse = [-x for x in gifts]
        hq.heapify(inverse)
        
        for _ in range(k):
            maxGifts = hq.heappop(inverse)

            res = floor(sqrt(abs(maxGifts)))

            hq.heappush(inverse,-res)


        return -sum(inverse)