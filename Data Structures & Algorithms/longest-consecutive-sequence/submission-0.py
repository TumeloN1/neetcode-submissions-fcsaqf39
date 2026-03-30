class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        items = set(nums)
        seqs = {}
        for num in nums:
            if num - 1 not in items:
                seqs[num] = [num]
        
        for start in seqs.keys():
            while seqs[start][-1] + 1 in items:
                seqs[start].append(seqs[start][-1] + 1)
        
        seqs = list(seqs.values())
        seqs = sorted(seqs, key=lambda x:len(x))
        return len(seqs[-1])