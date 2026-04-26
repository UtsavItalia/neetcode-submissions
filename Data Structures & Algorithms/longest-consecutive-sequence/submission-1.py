class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        result = 0

        print(elements)

        for num in nums:
            streak = 0
            curr = num
            while curr in elements:
                streak += 1
                curr += 1
            result = max(result, streak)
        return result
