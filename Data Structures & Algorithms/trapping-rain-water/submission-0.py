class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMost = height[left]
        rightMost = height[right]

        water = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                leftMost = max(leftMost, height[left])
                if height[left] < leftMost:
                    water += leftMost - height[left]
            
            else:
                right -= 1
                rightMost = max(rightMost, height[right])
                if height[right] < rightMost:
                    water += rightMost - height[right]

        return water