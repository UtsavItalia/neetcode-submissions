class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        mostWater = float('-inf')
        while i < j:
            currWater = min(heights[i], heights[j]) * (j - i)
            if currWater > mostWater:
                mostWater = currWater
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return mostWater