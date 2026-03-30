class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFreq = {}
        for num in nums:
            if num in mostFreq.keys():
                mostFreq[num] += 1
            else:
                mostFreq[num] = 1
        inOrder = sorted(mostFreq.items(), key=lambda x: x[1], reverse=True)
        return [inOrder[i][0] for i in range(k)]

        
