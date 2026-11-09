class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_size = min(len(word1), len(word2))
        
        res = []
        for i in range(min_size):
            res.append(word1[i])
            res.append(word2[i])

        res.append(word1[min_size:])
        res.append(word2[min_size:])

        return "".join(res)