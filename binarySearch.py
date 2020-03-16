# coding=utf-8

"""
二分查找，相关总结
参考博客链接：https://www.cnblogs.com/kyoner/p/11080078.html
"""


def binary_search1(nums: list, target: int) -> int:
    """
    在有序数组中，查找指定元素。存在则返回索引值，否则返回-1.
    :param nums: a list contain integer numbers
    :param target: searching target
    :return: the index of the target
    """
    # init searching zone [left, right]
    left, right = 0, len(nums) - 1

    # searching
    while left <= right:
        mid = left + (right - left) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # update searching zone [mid+1, right]
            left = mid + 1
        else:
            # update searching zone [left, mid-1]
            right = mid - 1
    return -1


def binary_search2(nums: list, target: int) -> int:
    """
    在有序数组中查找某个数的左边界
    数组是有序的，可能存在相同的值
    :param nums: a list contain integer numbers
    :param target: searching target
    :return: the index of the target
    """
    print(nums, target)
    # init searching zone [left, right)
    left, right = 0, len(nums)
    # searching
    while left < right:
        mid = left + (right - left) // 2
        print(left, right, mid)
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            # update searching zone [mid+1, right
            left = mid + 1
        else:
            # update searching zone [left, mid-1)
            right = mid

    return left


def mySqrt(target: int) -> int:
    """
    套用二分查找，查找右边界问题的解法
    这道题目可以理解为： 从[0, x]间找出，平方值小于等于X的右边界
    """
    if target <= 1:
        return target

    left, right = 0, target
    while left < right:
        mid = left + (right - left) // 2
        tmp = mid ** 2

        if tmp == target:
            return mid
        elif tmp < target:
            left = mid + 1
        else:
            right = mid

    return right - 1


if __name__ == "__main__":
    print(mySqrt(0))
