class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = dict(Counter(s))
        t_counter = dict(Counter(t))

        if s_counter == t_counter:
            return True
        else:
            return False