import sys


def cal_sqrt(num):
    start = 1
    end = num
    e = 0.01
    minus_result = sys.maxsize
    middle = 0
    while abs(minus_result) > e:
        middle = (start + end) / 2
        minus_result = middle * middle - num

        if minus_result > 0:
            end = middle
        else:
            start = middle

    return middle
