# coding=utf-8
from typing import Tuple, Any

from MyUtils import *


def getMid(head: ListNode):
    """
    获取链表中心节点，
    如果链表节点数为偶数，则返回右侧中心节点（slow指向的链表节点），此时fast为空
    如果链表节点是奇数，则返回中心节点（slow指向的链表节点），此时fast指向倒数第一个节点
    :param head: 链表头节点
    :return:
    """
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow, fast


def cutLink(head: ListNode, n: int) -> ListNode:
    """
    从单链表切除N个节点，并返回剩余部分的头节点
    :param head:
    :param n:
    :return:
    """
    if not head or n <= 0:
        return head

    cursor = head
    cnt = n - 1
    while cursor and cnt > 0:
        cursor = cursor.next
        cnt -= 1
    nextNode = None
    if cursor:
        nextNode = cursor.next
        cursor.next = None
    return nextNode


# 自底向上，归并排序
def sortList(head: ListNode) -> ListNode:
    # 链表长度
    cnt = 0
    cur = head
    while cur:
        cnt += 1
        cur = cur.next

    step = 0
    dummy = ListNode(0)
    tail = dummy
    while 2 ** step < cnt:
        # 步长是2**i
        # 每次取两个步长的链表，进行合并
        print("step is %d" % step)

        cursor = head
        # 循环截取两个步长的链表
        while cursor:
            cntA, cntB = 0, 0

            # 截取第一个子链
            temp_linkA = ListNode(0)
            temp_linkA.next = cursor
            tailA = temp_linkA
            while cursor and cntA < 2 ** step:
                cntA += 1
                tailA = cursor
                cursor = cursor.next
            print("cntA is %d" % cntA)
            tailA.next = None

            # 截取第二个子链
            temp_linkB = ListNode(0)
            temp_linkB.next = cursor
            tailB = temp_linkB
            while cursor and cntB < 2 ** step:
                cntB += 1
                tailB = cursor
                cursor = cursor.next
            print("cntB is %d" % cntB)
            tailB.next = None

            # 归并两个子链（已经排好序），追加到dummy后
            merged, merge_tail = mergeTwoSortedLink(temp_linkA.next, temp_linkB.next)
            tail.next = merged
            tail = merge_tail

        head = dummy.next
        # 下一个归并区间
        step += 1

    return head


def mergeTwoSortedLink(headA: ListNode, headB: ListNode) -> Tuple[Any, Any]:
    dummy = ListNode(float('-inf'))
    tail = dummy
    curA, curB = headA, headB
    while curA and curB:
        if curA.val < curB.val:
            tail.next = curA
            tail = curA
            curA = curA.next
        else:
            tail.next = curB
            tail = curB
            curB = curB.next
    if curA:
        tail.next = curA
    if curB:
        tail.next = curB

    while tail.next:
        tail = tail.next

    print_linklist(dummy.next)
    return dummy.next, tail


def test_getMid(lst):
    link = construct_linklist(lst)
    mid = getMid(link)
    print(mid.val)


def test_cutLink():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    link = construct_linklist(lst)
    print_linklist(link)
    rest = cutLink(link, 2)

    if rest:
        print_linklist(rest)
        print_linklist(link)
    else:
        print("Rest link is None")


if __name__ == "__main__":
    # test_getMid([1])
    # test_getMid([1, 2, 3, 4])
    # test_getMid([1, 2, 3, 4, 5])
    # test_cutLink()
    link = construct_linklist([1,2,3,4, 5])
    mid, fast = getMid(link)
    if mid:
        print(mid.val)
    else:
        print("mid is None")
        
    if fast:
        print(fast.val)
    else:
        print("fast is None")
