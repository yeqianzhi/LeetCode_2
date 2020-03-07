# coding:utf-8

"""
107. 二叉树的层次遍历 II

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [3,9,20,null,null,15,7]
class Solution:
    def levelOrderBottom(self, root):

        if root is None:
            return []

        queue = [root]  # queue = [3]
        res = []
        while queue:
            alist = []
            for i in range(len(queue)):  # len(queue) = 1
                cur = queue.pop(0)  # cur = [3], queue = []
                alist.append(cur.val)  # alist = [3]
                if cur.left:
                    queue.append(cur.left)  # queue = [9, 20]
                if cur.right:
                    queue.append(cur.right)
            res.append(alist)  # res = [3]
        return res[::-1]
