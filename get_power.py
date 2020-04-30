# -*- coding: utf-8 -*-#
# Name:         get_power
# Author:       ARCHI
# Date:         2020/4/8
# Description:  
# -------------------------------------------------------------------------------

def getPower(k: int, n:int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return k

    half = n // 2
    res = n % 2
    return getPower(k, half) * getPower(k, half) * getPower(k, res)



if __name__ == "__main__":
    lst = [1, 3, 7, 10, 17, 19, 49, 100]
    for i in range(1, 100):
        temp_abs_sum = 0
        for e in lst:
            temp_abs_sum += abs(e-i)

        print(i, '====', temp_abs_sum)