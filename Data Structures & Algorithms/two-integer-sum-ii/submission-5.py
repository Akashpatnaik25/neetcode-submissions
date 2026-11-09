class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                return [seen[comp] + 1, i + 1]  # Added + 1 for 1-indexing
            seen[num] = i
        return []