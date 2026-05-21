import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]

        hq.heapify(stones)

        while len(stones) > 1:
            s1 = hq.heappop(stones)
            s2 = hq.heappop(stones)

            if s1 != s2:
                res = abs(s1-s2)
                hq.heappush(stones,-res)

        return -stones[0] if stones else 0