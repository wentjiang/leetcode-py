from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        result = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                result += 1
        return result
