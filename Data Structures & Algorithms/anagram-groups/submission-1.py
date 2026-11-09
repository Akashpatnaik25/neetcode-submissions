class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_map = {}

        for word in strs:
            current = "".join(sorted(word))
            print(word)
            if word_map.get(current):
                word_map[current] += [word]
            else:
                word_map[current] = [word]
        
        
        return [item for item in word_map.values()]
        