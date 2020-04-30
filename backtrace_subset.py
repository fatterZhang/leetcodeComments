# -*- coding: utf-8 -*-#
# Name:         subset
# Author:       ARCHI
# Date:         2020/4/27
# Description:  回溯法求，数组所有子集
# 参考链接：https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/zi-ji-pai-lie-zu-he#er-zu-he
# -------------------------------------------------------------------------------

from typing import List

rst = []


def getSubset(nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
        return rst
    backtrace(nums, 0, [])
    return rst


def backtrace(nums: List[int], start: int, path: List[int]):
    rst.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrace(nums, i + 1, path)
        path.pop()


if __name__ == "__main__":
    print(getSubset([i for i in range(4)]))
