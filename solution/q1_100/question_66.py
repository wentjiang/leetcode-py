from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for i in range(len(digits)):
            sum += int(digits[i]) * (10 ** (len(digits) - i - 1))
        sum_str = str(1 + sum)
        return [int(j) for j in sum_str]
