class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for element in strs[1:]:
            while element[:len(prefix)] != prefix :
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

                