# -*- coding: utf-8 -*-#
# Name:         1095_mountainArray
# Author:       ARCHI
# Date:         2020/4/29
# Description:  mountainArray: 递增递减数组，左侧递增，右侧递减
# -------------------------------------------------------------------------------
from typing import List

# 找到最值
def getMountainArrayPeak(nums:List[int]):
    left, right = 0, len(nums)
    while left < right-1:
        mid = left + (right-left)//2
        print(nums[left:mid], nums[mid], nums[mid+1:right+1])
        if nums[mid] < nums[mid+1]:
            left = mid
        else:
            right = mid
        print(nums[left:right+1])
    return left if nums[left]>nums[right] else right

if __name__ == "__main__":
    lst = [1,5,4]
    print(getMountainArrayPeak(lst))
