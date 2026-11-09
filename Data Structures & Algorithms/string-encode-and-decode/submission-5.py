class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for i in range(0,len(strs)):
            encoded_str +=  f"{len(strs[i])}#{strs[i]}"   
        # encoded_str = f"{secret}".join(strs)
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != "#":
                j+=1
            count = int(s[i:j])
            decoded_list.append(s[j+1:j+1+count])
            i = j+1+count

        # decoded_list = s.split("#*")
        return decoded_list