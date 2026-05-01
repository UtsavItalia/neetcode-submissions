class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        window_counter = dict()

        for i in range(len(s1)):
            window_counter[s2[i]] = window_counter.get(s2[i], 0) + 1
        
        if window_counter == s1_counter:
            return True

        for i in range(len(s1), len(s2)):
            window_counter[s2[i]] = window_counter.get(s2[i], 0) + 1
            left_char = s2[i - len(s1)]
            window_counter[left_char] -= 1

            if window_counter[left_char] == 0:
                del window_counter[left_char]

            if window_counter == s1_counter:
                return True

        return False