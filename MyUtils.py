# -*- coding: utf-8 -*-#
# Name:         MyUtils
# Author:       ARCHI
# Date:         2020/3/16
# Description:  
# -------------------------------------------------------------------------------

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def construct_linklist(lst: List[int]) -> ListNode:
    rst = ListNode(0)
    tail = rst
    for ele in lst:
        tail.next = ListNode(ele)
        tail = tail.next
    return rst.next


def print_linklist(head):
    cursor = head
    rst = []
    while cursor:
        rst.append(cursor.val)
        cursor = cursor.next
    print(' --> '.join([str(e) for e in rst]))
