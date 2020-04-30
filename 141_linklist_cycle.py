# -*- coding: utf-8 -*-#
# Name:         141_linklist_cycle
# Author:       ARCHI
# Date:         2020/3/17
# Description:  环形单链表相关的题目
# -------------------------------------------------------------------------------

from MyUtils import *

"""
相关考点：双指针， 检测是否存在环，找到环的入口

环形入口解题思路：参考142题解 “环形链表 II（双指针法，清晰图解）”
"""


# 判断是否存在环 ----时间复杂度：O(n), 空间复杂度： O(N)
def detectCycle1(head: ListNode) -> bool:
    """
    利用查找表，记录访问记录
    :param head:
    :return:
    """
    visit_table = set()
    cur = head
    while cur:
        if cur in visit_table:
            return True
        else:
            visit_table.add(cur)
        cur = cur.next
    return False


# 判断是否存在环 ----时间复杂度：O(n), 空间复杂度： O(1)
def detectCycle2(head: ListNode) -> bool:
    """
    利用快慢指针，记录访问记录
    :param head:
    :return:
    """
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


# 找到环入口 ---- 时间复杂度：O(n), 空间复杂度： O(n)
def findCycleEntrance1(head: ListNode) -> bool:
    """
    利用快慢指针，记录访问记录
    :param head:
    :return:
    """
    visit_table = set()
    cur = head
    while cur:
        if cur in visit_table:
            return cur
        else:
            visit_table.add(cur)
        cur = cur.next
    return None


# 找到环入口 ---- 时间复杂度：O(n), 空间复杂度： O(1)
def findCycleEntrance2(head: ListNode) -> ListNode:
    fast, slow = head, head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        # 第一次相遇
        if fast == slow:
            fast = head
            # 第二次相遇
            while fast != slow:
                fast, slow = fast.next, slow.next
            return fast
    return None


def reorderList(self, head: ListNode) -> None:
    """
    截取右半部分
    将右半部分反转
    双指针逐个插入
    Do not return anything, modify head in-place instead.
    """
    # 节点个数大于1时才需要进行操作
    if head and head.next:
        # 快慢指针找中心节点
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        # 前半部分节点尾节点指针置空

        # 如果是奇数个节点，则将右半部分的起始节点右移一个
        right_start = slow.next if fast else slow
        # 将左半链表尾节点的指针置空
        cursor = head
        while cursor.next != right_start:
            cursor = cursor.next
        cursor.next = None

        # 右半链表反转
        dummy = ListNode(0)
        while right_start:
            next_node = right_start.next
            right_start.next = dummy.next
            dummy.next = right_start
            right_start = next_node

        # 反转后的链表逐个插入到左半链表
        cursor, right_start = head, dummy.next
        while right_start:
            next_node = right_start.next
            right_start.next = cursor.next
            cursor.next = right_start
            right_start = next_node






