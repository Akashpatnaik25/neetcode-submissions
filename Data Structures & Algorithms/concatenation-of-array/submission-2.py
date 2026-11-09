class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we simply copies the original array and did the contatencation
        return nums + nums[:]
        