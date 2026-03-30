class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        q = collections.deque() # contains indices
        while r < len(nums):
            # pop all smaller values from the q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove from the window if it's out of bounds
            if l > q[0]:
                q.popleft()
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res

