# -*- coding: utf-8 -*-#
# Name:         128_eligent_subarray
# Author:       ARCHI
# Date:         2020/4/21
# Description:  
# -------------------------------------------------------------------------------
from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    if len(nums) < k:
        return 0

    # 初始化窗口 (left, right]
    left, right = -1, 0
    odd_cnt = 0
    while right < len(nums):
        if nums[right] % 2 == 1:
            odd_cnt += 1
        if odd_cnt == k:
            break
        right += 1

    # 整个数组都不满足条件
    if odd_cnt != k:
        return 0

    rst = 0
    # 开始缩减左右区间指针
    print('beging zone ', left, right)
    while right < len(nums):
        # right指针向右移动，找到下一个奇数，记录下走的步数
        after = right + 1
        while after < len(nums) and nums[after] % 2 == 0:
            after += 1
        right_step = after - right
        right = after

        # left指针向右移动，找到
        after = left + 1
        while after <= right and nums[after] % 2 == 0:
            after += 1
        left_step = after - left
        left = after
        print(left_step, right_step)
        rst += left_step * right_step
    return rst


if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(numberOfSubarrays(nums, k))
