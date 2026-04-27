class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        mostWater = 0
        while i < j:
            currWater = min(heights[i], heights[j]) * (j - i)
            mostWater = max(mostWater, currWater)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return mostWater