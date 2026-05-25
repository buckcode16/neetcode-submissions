class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        # PHASE 1: The Initialization
        # 1. Use Counter(tasks) to get the frequencies.
        count = Counter(tasks)
        # 2. Extract just the counts, multiply by -1, and turn them into a valid heap using heapq.heapify()
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        # 3. Create an empty deque to act as the cooldown buffer.
        q = collections.deque()
        # 4. Initialize a 'time' variable to 0.
        t = 0
        
        # PHASE 2: The Time Loop
        # Run a while loop that continues as long as there is anything in the heap OR the deque.
        while maxHeap or q:
            
            # (Inside the loop)
            # The CPU cycle starts. Immediately increment 'time' by 1.
            t+=1
            
            
            # PHASE 3: The Execution Phase (Heap)
            # If the heap is not empty:
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
            # 1. Pop the top value (the most frequent task).
            # 2. Add 1 to it (since it's negative, adding 1 represents completing a task).
                cnt+=1
                
                # PHASE 4: The Quarantine Phase (Deque)
                # If the popped task still has a count remaining (count < 0):
                if cnt < 0:
                # Append a list/tuple to the deque: [remaining_count, unlock_time]
                # The unlock_time is exactly (time + n).
                    q.append([cnt,t+n])
                
                
            # PHASE 5: The Reactivation Phase (Deque to Heap)
            # Look at the oldest item in the deque (index 0).
            # If the deque is not empty AND the item's unlock_time == current time:
            if q and q[0][1] == t:
            # 1. Pop it from the left side of the deque.
            # 2. Push its count back into the heap so it can be executed again.
                heapq.heappush(maxHeap,q.popleft()[0])
            
            
        # Once both the heap and deque are completely empty, the loop ends.
        # Return the total 'time' elapsed.
        return t