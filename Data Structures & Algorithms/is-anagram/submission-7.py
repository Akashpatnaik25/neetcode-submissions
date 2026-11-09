class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        '''
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
        '''

        temp = [0] * 26

        for i in range(len(s)):
            char1 = ord(s[i]) - 97
            char2 = ord(t[i]) - 97

            temp[char1] += 1 
            temp[char2] -= 1  
            

        for i in range(len(temp)):
            if temp[i] != 0:
                return False

        return True        
            

        
        