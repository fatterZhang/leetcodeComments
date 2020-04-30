# -*- coding: utf-8 -*-#
# Name:         combine
# Author:       ARCHI
# Date:         2020/4/28
# Description:  回溯法，求解组合问题，
# 给定一个包含N个元素的数组(无重复), 输出所有K个元素的组合
# 参考链接：https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/zi-ji-pai-lie-zu-he#er-zu-he
# -------------------------------------------------------------------------------
from typing import List

rst = []
def getCombineK(nums:List[int], k:int)->List[List[int]]:
    if not nums:
        return rst
    backtrace(nums, 0, [], k)
    return rst


def backtrace(nums:List[int], start:int, path:List[int], k:int):
    # 判断终止
    if len(path) == k:
        rst.append(path[:])
        return

    # 在当前path的抉择点上，可做的选择有nums[start:]
    # 即选择把那个元素添加进，当前组合中
    for i in range(start, len(nums)):
        # 做选择
        path.append(nums[i])
        # 继续做下一次选择, 下一次可选择的有nums[i+1:]
        backtrace(nums, i+1, path, k)
        # 撤销当前选择，便于走其他选择路径
        path.pop()

if __name__ == "__main__":
    lst = [i for i in range(5)]
    print(getCombineK(lst, 3))