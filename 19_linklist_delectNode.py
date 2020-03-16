# -*- coding: utf-8 -*-#
# Name:         19_linklist_delectNode
# Author:       ARCHI
# Date:         2020/3/16
# Description:  
# -------------------------------------------------------------------------------

from MyUtils import *


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    双指针的思想
    删除倒数第N个节点，由于是单链表，需要找到倒数第N+1的节点
    因此front指针需要先走N+1步（提醒：这里的解法设置一个dummy头节点，以及题目中保证N有效）
    """
    # dummy头节点大法
    dummy = ListNode(0)
    dummy.next = head

    front, behind = dummy, dummy
    # front先走N+1步
    while n >= 0:
        front = front.next
        n -= 1
    # front, behind 同时走，知道front为空
    while front:
        front = front.next
        behind = behind.next

    # 删除behind后面的节点（即倒数第n节点）
    behind.next = behind.next.next

    return dummy.next