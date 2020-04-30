# -*- coding: utf-8 -*-#
# Name:         287_findDuplicate
# Author:       ARCHI
# Date:         2020/3/22
# Description:  
# -------------------------------------------------------------------------------
from typing import List


def findDuplicate(nums: List[int]) -> int:
    # 二分查找法，时间复杂度O(NlogN)

    bd_left, bd_right = 1, len(nums) - 1
    while bd_left < bd_right:
        print("current boundary [%d, %d]"%(bd_left, bd_right))
        mid = bd_left + (bd_right - bd_left) // 2
        print("searching zone is [%d, %d]" % (bd_left, mid))
        # 统计[bd_left, mid]间的个数
        cnt = 0
        for e in nums:
            if bd_left <= e <= mid:
                cnt += 1
        print("find %d nums"%cnt)

        if cnt > (mid - bd_left + 1):
            # 收缩右边界
            bd_right = mid
        else:
            # 收缩左边界
            bd_left = mid+1
        print("next boundary [%d, %d]"%(bd_left, bd_right))
    return bd_left

if __name__ == "__main__":
    lst = [3,1,3,4,2]
    print(findDuplicate(lst))