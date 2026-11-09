class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}

        for word in strs:
            # Sort characters to create a common key for anagrams
            current = "".join(sorted(word))

            # If key already exists, add word to the existing group
            if word_map.get(current):
                word_map[current] += [word]
            else:
                # Create a new group for this anagram pattern
                word_map[current] = [word]

        # Return all grouped anagrams
        return [item for item in word_map.values()]