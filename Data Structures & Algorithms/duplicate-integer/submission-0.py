class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for num in nums:
            if num in values.keys():
                return True
            else:
                values[num] = 0
        return False