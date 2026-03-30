class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [0]
        curr = 1
        while stack and curr < len(temperatures):
            while stack and temperatures[curr] > temperatures[stack[-1]]:
                i = stack.pop()
                result[i] = curr - i
            stack.append(curr)
            curr += 1
        return result

