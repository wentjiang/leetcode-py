class Solution:
    temp = dict()

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n - 1 in self.temp:
            stair_n_1 = self.temp[n - 1]
        else:
            stair_n_1 = self.climbStairs(n - 1)
            self.temp[n - 1] = stair_n_1

        if n - 2 in self.temp:
            stair_n_2 = self.temp[n - 2]
        else:
            stair_n_2 = self.climbStairs(n - 2)
            self.temp[n - 2] = stair_n_2

        return stair_n_1 + stair_n_2
