class Solution:
    def validPalindrome(self, s: str) -> bool:
        p = "".join([i for i in s if s.isalnum()])
        if p == p[::-1] :
            return True
        unique = set(p)
        for i in unique :
            j = p.replace(i,"")
            if j == j[::-1]:
                return True
        return False

        