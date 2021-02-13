from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
           if hash_table.get(i) == None:
               hash_table[i] = 1
           else:
               hash_table.pop(i)
        return hash_table.popitem()[0]

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a