class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in result:
                result[sortedStr].append(s)
            else:
                result[sortedStr] = [s]
        return list(result.values())
