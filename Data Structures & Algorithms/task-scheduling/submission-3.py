class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()


        while q or maxHeap:
            t+=1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt+=1

                if cnt < 0:
                    q.append([cnt, t+n])


            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])


        return t

            