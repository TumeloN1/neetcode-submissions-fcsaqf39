class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       diffs = {}

       for i, num in enumerate(nums):
            if num in diffs.keys():
                return list((diffs[num], i))
            diffs[target - num] = i