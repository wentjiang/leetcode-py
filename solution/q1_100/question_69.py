class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        _max = x / 2
        _min = 0
        while _min < _max:
            _mid = (_min + _max + 1) // 2
            if _mid ** 2 <= x <= (_mid + 1) ** 2:
                return int(_mid + 1) if x == (_mid + 1) ** 2 else int(_mid)
            if _mid ** 2 > x:
                _max = _mid
            else:
                _min = _mid
        return x
