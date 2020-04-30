# -*- coding: utf-8 -*-#
# Name:         tree_traversal
# Author:       ARCHI
# Date:         2020/4/13
# Description:  二叉树的各种遍历（非递归）
# 参考链接：https://blog.csdn.net/Benja_K/article/details/88389039
# -------------------------------------------------------------------------------
from typing import List


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution(object):

    def preOrder(self, root: TreeNode) -> List[TreeNode]:
        rst = []
        if root:
            stack = [root]

            while len(stack):
                cur_node = stack.pop()
                rst.append(cur_node.value)

                if cur_node.right:
                    stack.append(cur_node.right)

                if cur_node.left:
                    stack.append(cur_node.left)
        return rst

    def preOrderTraversal(self, root:TreeNode) ->List[int]:
        rst = []
        if not root:
            return rst

        stack = []
        cursor = root    # 游标初始化，指向根节点
        while cursor or stack:
            # 因为是前序遍历，游标第一次遇到某个节点时，就执行访问操作
            # 第一次遇到时，需要入栈的目的是为了找到右子树
            if cursor:
                stack.append(cursor)         # 第一次遇到，入栈
                rst.append(cursor.value)     # 根据要求，执行访问操作
                cursor = cursor.left         # 游标移动到左子树
            else:
                temp_node = stack.pop()      # 第二次遇到，仅出栈(目的是找到右子树节点)
                cursor = temp_node.right
        return rst

    def midOrderTraversal(self, root:TreeNode) ->List[int]:
        rst = []
        if not root:
            return rst

        stack = []
        cursor = root    # 游标初始化，指向根节点
        while cursor or stack:
            # 因为是中序遍历，游标第二次遇到某个节点时，才执行访问操作
            # 第一次遇到时，需要入栈的目的是为了找到右子树
            if cursor:
                stack.append(cursor)         # 第一次遇到，入栈
                cursor = cursor.left         # 游标移动到左子树
            else:
                temp_node = stack.pop()      # 出栈，目的是找到右子树节点
                rst.append(temp_node.value)  # 第二次遇到，执行相关访问操作
                cursor = temp_node.right
        return rst

    def postOrderTraversal(self, root:TreeNode) -> List[int]:
        rst = []
        if not root:
            return rst

        stack = []      # 栈
        flag = []       # 标记栈中节点访问次数
        cursor = root   # 初始化游标，指向整棵树的根节点
        while cursor or stack:

            # 游标不为空，前进方向是向下的
            if cursor:
                stack.append(cursor)   # 第一次遇到，入栈
                flag.append(1)         # 并标记第几次遇到
                cursor = cursor.left   # 游标移动到左子树

            # # 游标为空，前进方向是向上的
            # else:
            #     # 第二次遇到某节点，不出栈，只读取
            #     if flag[-1] == 1:
            #         flag[-1] += 1              # 更新遇到的次数
            #         cursor = stack[-1].right   # 游标移动到右子树
            #     # 第三次遇到，出栈并执行访问
            #     else:
            #         temp = stack.pop()
            #         rst.append(temp.value)
            #         cursor = None

            # 第二次遇到某节点，不出栈，只读取
            elif flag[-1]:
                flag[-1] += 1              # 更新遇到的次数
                cursor = stack[-1].right   # 游标移动到右子树
            # 第三次遇到，出栈并执行访问
            else:
                temp = stack.pop()
                rst.append(temp.value)

                flag.pop()
                cursor = None











