class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        have, need = 0, len(t_counter)
        window_counter = dict()

        left = 0
        result = ""

        for right in range(len(s)):
            window_counter[s[right]] = window_counter.get(s[right], 0) + 1

            if s[right] in t_counter and t_counter[s[right]] == window_counter[s[right]]:
                have += 1

            while have == need:
                if not result or (right - left + 1) < len(result):
                    result = s[left:right + 1]
                
                char_left = s[left]
                window_counter[char_left] -= 1

                if char_left in t_counter and window_counter[char_left] < t_counter[char_left]:
                    have -= 1
                left += 1

        return result