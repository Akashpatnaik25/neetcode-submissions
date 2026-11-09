class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_count1 = {}
        freq_count2 = {}

        for char in s:
            freq_count1[char] = freq_count1.get(char, 0) + 1

        for char in t:
            freq_count2[char] = freq_count2.get(char, 0) + 1

        for char in freq_count1:
            if freq_count1.get(char, 0) != freq_count2.get(char, 0):
                return False

        return True

        
        