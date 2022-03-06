# 正整数求解开方,误差小于0.01
def sqrt_num(num):
    first = 1
    second = num

    iteration_times = 0
    middle = 0
    minus_result = middle * middle - num
    e = 0.01
    while abs(minus_result) > e:
        iteration_times += 1
        middle = (first + second) / 2
        minus_result = middle * middle - num
        if minus_result >= 0:
            second = middle
        else:
            first = middle
    return middle
