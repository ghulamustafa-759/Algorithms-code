class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums:
                if i + j == target:
                    return i,j