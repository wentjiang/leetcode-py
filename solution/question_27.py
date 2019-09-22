from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort();
        n = len(nums)
        num = 0
        for i in range(n):
            if nums[i] == val:
                num += 1
            else:
                nums[i - num] = nums[i]
        return n - num

    def removeElement1(self, nums: List[int], val: int) -> int:
        nums.remove(val)
        return nums


