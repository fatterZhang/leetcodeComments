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


def deleteDuplicates(head: ListNode) -> ListNode:
    """
    删除有序链表中的重复元素
    dummy头节点
    双指针
    """
    dummy = ListNode(float('-inf'))
    cursor, tail = head, dummy

    while cursor:
        if cursor.val != tail.val:
            tail.next = cursor
            tail = cursor
            cursor = cursor.next
            tail.next = None
        else:
            cursor = cursor.next
    return dummy.next


def deleteDuplicates1(head: ListNode) -> ListNode:
    """
    删除无序链表中的重复元素
    查找表
    dummy头节点
    双指针
    """
    dummy = ListNode(float('-inf'))
    cursor, tail = head, dummy
    found = set()

    while cursor:
        if cursor.val not in found:
            found.add(cursor.val)

            tail.next = cursor
            tail = cursor
            cursor = cursor.next
            tail.next = None
        else:
            cursor = cursor.next
    return dummy.next


if __name__ == "__main__":
    lst = [7, 9, 1, 1, 1, 2, 3, 4, 4, 5]
    link = construct_linklist(lst)
    print_linklist(deleteDuplicates1(link))
