class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        #[2,20,4,10,3,4,5]
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                currLen = 1
                while num + currLen in numSet:
                    currLen += 1
                longest = max(currLen, longest)
        return longest
