# coding=utf-8

"""
二分查找，相关总结
参考博客链接：https://www.cnblogs.com/kyoner/p/11080078.html
"""


def binary_search1(nums, target):
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
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # update searching zone [mid+1, right]
            left = mid + 1
        else:
            # update searching zone [left, mid-1]
            right = mid - 1
        print("----", left, right)

    # 如果没有找到, left 就是待插入的位置
    return left, mid


# 寻找最左元素
def binary_search2(nums: list, target: int) -> int:
    """
    在有序数组中查找某个数的左边界
    数组是有序的，可能存在相同的值
    :param nums: a list contain integer numbers
    :param target: searching target
    :return: the index of the target
    """
    # init searching zone [left, right)
    left, right = 0, len(nums) - 1
    # searching
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target: right = mid
        elif nums[mid] < target: left = mid + 1   # update searching zone [mid+1, right)
        else: right = mid                         # update searching zone [left, mid-1)

    # left 的含义是：数组nums中比target小的元素个数
    # 即nums[0:left] 中的元素都是小于target
    # 至于nums[left] 是否等于target需要判断
    # if left >= len(nums) or nums[left] != target:
    #     print("Target not in nums")
    # else:
    #     print("Find target at index: %d" % left)
    return left


# 寻找最右元素
def binary_search3(nums: list, target: int) -> int:
    left, right = -1, len(nums) - 1
    # init searching zone (left, right]
    while left < right:
        mid = right - (right - left) // 2
        if nums[mid] == target:left = mid  # update zone (left, right]
        elif nums[mid] < target:left = mid  # update zone (mid+1, right]
        else:right = mid - 1  # update zone (left, mid-1]

    if left>=len(nums) or nums[left]!=target:
        print("Target not in nums")
    else:
        print("Find target at index: %d" % left)

    return left


def mySqrt(target: int) -> int:
    """
    套用二分查找，查找右边界问题的解法
    这道题目可以理解为： 从[0, x]间找出，平方值小于等于X的右边界
    """
    if target <= 1:
        return target

    left, right = 0, target // 2 + 1
    while left < right:
        mid = left + (right - left) // 2
        tmp = mid ** 2
        # print(left, right, mid, tmp)

        if tmp == target:
            return mid
        elif tmp < target:
            left = mid + 1
        else:
            right = mid

    return right - 1


def letterCombinations(digits: str):
    if not str:
        return []

    chars = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    dct = {}
    for i in range(2, 10):
        dct[str(i)] = list(chars[i - 2])
    print(dct)

    dights = list(digits)
    from collections import deque
    rst = deque(dct[digits[0]])
    print(rst)
    for e in digits[1:]:
        cnt = len(rst)
        for i in range(cnt):
            temp = rst.popleft()
            for y in dct[e]:
                rst.append(temp + y)
        print(rst)

    return rst


if __name__ == "__main__":
    lst = [0, 1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 8, 10]
    # print(binary_search1(lst, -1))
    print(binary_search3(lst, 7))
    # for i in range(100):
    #     print(i, '  ', mySqrt(i))

    # print(letterCombinations('234'))
