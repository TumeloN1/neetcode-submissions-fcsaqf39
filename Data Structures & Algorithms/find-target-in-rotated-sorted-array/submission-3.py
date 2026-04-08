class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: # found
                return mid

            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:  # target is in the sorted left half
                    r = mid - 1
                else:                              # target must be in the right half
                    l = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:  # target is in the sorted right half
                    l = mid + 1
                else:                              # target must be in the left half
                    r = mid - 1

        return -1