class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char not in pairs.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if pairs[stack.pop()] != char:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
