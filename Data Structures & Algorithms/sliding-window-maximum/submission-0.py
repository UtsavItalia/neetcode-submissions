class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        result = []
        for i in range(k):
            window.append(nums[i])
        
        result.append(max(window))

        for i in range(k, len(nums)):
            window.pop(0)
            window.append(nums[i])
            result.append(max(window))

        return result