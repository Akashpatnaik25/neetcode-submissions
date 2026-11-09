class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_dict = {}
        second_dict = {}
        if len(s) != len(t):
            return False
        i = j = 0
        while i< len(s):
            if s[i] not in first_dict:
                first_dict[s[i]] = 1
                
            else:
                first_dict[s[i]] += 1
            
            if  t[i] not in second_dict:
                second_dict[t[j]] = 1
            else:
                second_dict[t[j]] += 1

            i +=1
            j +=1
        return first_dict == second_dict
