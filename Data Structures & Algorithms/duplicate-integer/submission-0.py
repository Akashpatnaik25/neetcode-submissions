class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = set()
        for element in nums:
            if element in contains:
                return True
            else:
                contains.add(element)
        return False
