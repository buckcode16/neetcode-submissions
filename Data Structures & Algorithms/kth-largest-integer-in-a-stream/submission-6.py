import heapq as hp

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        hp.heapify(self.h)
        for n in nums:
            if len(self.h) == k:
                hp.heappushpop(self.h,n)
            else:
                hp.heappush(self.h,n)

            

    def add(self, val: int) -> int:
        if len(self.h) == self.k:
            hp.heappushpop(self.h,val)
        else:
            hp.heappush(self.h,val)

        return self.h[0]
        


        
