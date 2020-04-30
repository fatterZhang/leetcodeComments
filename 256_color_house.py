# -*- coding: utf-8 -*-#
# Name:         256_color_house
# Author:       ARCHI
# Date:         2020/3/19
# Description:  
# -------------------------------------------------------------------------------
from typing import List


def minColorCost(costs: List[List[int]]) -> int:
    if len(costs) < 1:
        return 0
    min_cost = costs[0]
    for e in costs[1:]:
        temp = min_cost.copy()
        min_cost[0] = min(temp[1], temp[2]) + e[0]
        min_cost[1] = min(temp[0], temp[2]) + e[1]
        min_cost[2] = min(temp[1], temp[0]) + e[2]

    return min(min_cost)

if __name__ == "__main__":
    from math import log, e
    for i in range(1, 100):
        p = i/100
        q = 1-p
        # print(p, q)
        s = -p*log(p, e) - q*log(q, e)
        print(round(s, 4))