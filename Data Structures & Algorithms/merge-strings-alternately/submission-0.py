class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        w1 = len(word1)
        w2 = len(word2)
        result = ""
        while i < w1 and j < w2:
            result += (word1[i] + word2[j])
            i +=1
            j +=1
        
        result += word1[i:]
        result += word2[j:]
        return result