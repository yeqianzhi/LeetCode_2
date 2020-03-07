# coding:utf-8

"""
101. 对称二叉树

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

"""


class Solution:
    def isSymmetric(self, root):

        """
        分成两个二叉树，t1,t2
        t1.left == t2.right
        t1.right == t2.left

        :param root:
        :return:
        """
        def isMirror(t1, t2):

            if (not t1) and (not t2):
                return True

            if (not t1) or (not t2):
                return False

            if t1.val != t2.val:
                return False

            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root, root)


