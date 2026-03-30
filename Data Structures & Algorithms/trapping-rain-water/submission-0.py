class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        two pointer approach
        start with the pointers on the ends of the array
        initialize highest height on each side
        while the two pointers have not collided we:
            check if the left is smaller, if it is we move it inward and update the leftmax
            we then add the difference between leftmax and current height to the total and continue
            vice versa for right
        approach works by identifying which height(left, right) is the limiter at each stage and then adding
        the water trapped on that side only.
        much simpler than trying to sweep across the array and trying to partition it into valleys where water is trapped as 
        there are too many ways to create a valley
        '''
        left = 0
        right = len(height) - 1
        lMax, rMax = height[left], height[right]
        res = 0
        while left < right:
            if lMax < rMax:
                left += 1
                lMax = max(lMax, height[left])
                res += lMax - height[left]
            else:
                right -= 1
                rMax = max(rMax, height[right])
                res += rMax - height[right]
        return res