class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        i = 0
        while i < len(nums):
            print(seen)
            neededNum = target - nums[i]
            if neededNum in seen:
                return [seen[neededNum], i]
            else:
                seen[nums[i]] = i
                i += 1
        return []