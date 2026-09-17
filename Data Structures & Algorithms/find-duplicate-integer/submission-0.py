class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        could solve it with no extra space in nlogn by just sorting the array
        could also create a visited set that just tells me which numbers ive seen but thats O(n) extra space
        is this a bit manipulation thing?? but thats extra memory too
        '''
        # Phase 1: find a meeting point inside the cycle
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find the cycle entrance (the duplicate)
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow