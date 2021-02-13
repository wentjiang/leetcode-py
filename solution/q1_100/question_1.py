from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result = {}
        for i in range(n):
            temp = target - nums[i]
            if temp in result:
                return [result[temp],i]
            result[nums[i]] = i
