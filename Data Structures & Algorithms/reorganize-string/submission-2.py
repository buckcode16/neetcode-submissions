class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count = Counter(s)

        maxHeap = [[-cnt, c] for c, cnt in count.items()]
        heapq.heapify(maxHeap)
        res = ""
        prev =  None

        # loop condition: if heap has element 
        # or prev still has element so we can check final early exit
        while maxHeap or prev:

        # early exit if only prev exists, appending prev to 
        # string would end up with the same char back-to-back 
            if prev and not maxHeap:
                return ""

        # pop
            cnt, c = heapq.heappop(maxHeap)
            res+=c
            cnt+=1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None

        # isolate current highest, cause we need to return the holding prev
        # to the heap in next iteration
            if cnt != 0:
                prev = [cnt, c]

        return res

            
