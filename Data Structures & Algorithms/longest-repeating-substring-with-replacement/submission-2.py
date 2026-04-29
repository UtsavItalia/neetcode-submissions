class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        longest = float('-inf')
        left = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            
            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return int(longest)