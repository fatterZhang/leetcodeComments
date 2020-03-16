# coding=utf-8
# 链表的插入排序法
from MyUtils import *


def insertionSortList(head: ListNode) -> ListNode:
    dummy = ListNode(float('-inf'))
    tail = dummy

    current = head
    while current:
        # 插入到尾部节点后的情况
        if current.val >= tail.val:
            tail.next = current
            tail = current
            current = current.next
            tail.next = None
        # 插入到链表中间的某个位置的情况
        else:
            # 保存下一个节点信息
            temp_node = current.next
            # tail.next = temp_node

            # 这里面应用了一个小技巧，设置了头节点。
            # 从头节点dummy开始，找到插入位置(该节点的next节点值比current节点值大)
            # 找到后在节点后插入current节点即可
            cursor = dummy
            while cursor.next and cursor.next.val < current.val:
                cursor = cursor.next

            # 插入到结果链表中
            current.next = cursor.next
            cursor.next = current

            # 更新下一个待检测的节点
            current = temp_node
            print_linklist(dummy.next)
    return dummy.next


if __name__ == "__main__":
    lst = [4, 2, 1, 3]
    link = construct_linklist(lst)
    print_linklist(link)
    insertionSortList(link)
