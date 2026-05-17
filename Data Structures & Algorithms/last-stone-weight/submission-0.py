import heapq as hp
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        hp.heapify(stones)
        while len(stones) > 1:
            r1 = -hp.heappop(stones)
            r2 = -hp.heappop(stones)

            if r1 != r2:
                v = abs(r1 - r2)
                hp.heappush(stones, -v)

        return 0 if not len(stones) else -stones[0]