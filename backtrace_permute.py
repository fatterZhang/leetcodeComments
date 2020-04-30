# -*- coding: utf-8 -*-#
# Name:         permute
# Author:       ARCHI
# Date:         2020/4/27
# Description:  回溯法，全排列
# 参考链接：https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/zi-ji-pai-lie-zu-he#er-zu-he
# -------------------------------------------------------------------------------
from typing import List

rst = []
def myPermute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
        return rst

    flag = [0]*len(nums)
    backTrace(nums, [], flag)
    return rst


def backTrace(nums: List[int], path: List[int], flag:List[int]):
    # 结束判断：如果路径长度等于nums中元素个数，表示路径已经走到头
    if len(path) == len(nums):
        rst.append(path[:])
        return

    # 在当前path的抉择点上，可做的选择有 set(nums)-set(path)
    # 即选择把那个元素添加进，当前排列中
    for i in range(len(nums)):
        # 如果当前的选择，已经使用过，则跳过
        if flag[i]:
            continue
        else:
            # 执行某个选择，并将是否使用位置1
            path.append(nums[i])
            flag[i] = 1

            # 基于当前的选择，继续做下一次的选择
            backTrace(nums, path, flag)

            # 撤销当前选择，便于执行其他可能的选择
            path.pop()
            flag[i] = 0


if __name__ == "__main__":
    print(myPermute([1, 2, 3, 4]))
