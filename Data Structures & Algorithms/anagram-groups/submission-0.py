class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)
        for element in strs:
            sorted_str = ''.join(sorted(element))
            res_dict[sorted_str].append(element)
        return list(res_dict.values())