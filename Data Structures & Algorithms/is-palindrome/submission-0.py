class Solution:
    def isPalindrome(self, s: str) -> bool:
        def convert(ele:str):
            t = ord(ele)
            if 48 <= t <= 57 :
                return ele
            elif 65 <= t <= 90 :
                return ele.lower()
            elif 97 <= t <= 122 :
                return ele
            return ""
        st = ""
        for i in s : 
            st +=convert(i)
        i = 0 
        j = len(st) - 1
        while i < j :
            if st[i] != st[j]:
                return False
            i += 1
            j -=1 
        return True