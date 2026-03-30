from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = deque() # This will store INDICES
        res = []
        
        for i in range(len(nums)):
            # 1. Discard smaller elements from the back
            # They can never be the max if a newer, larger element exists
            while mq and nums[i] > nums[mq[-1]]:
                mq.pop()
            
            mq.append(i)
            
            # 2. Remove the front element if it's out of the window range
            if mq[0] == i - k:
                mq.popleft()
            
            # 3. If we've reached the window size k, the front is our max
            if i >= k - 1:
                res.append(nums[mq[0]])
                
        return res
