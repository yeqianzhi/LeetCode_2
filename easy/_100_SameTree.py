# coding:utf-8

"""
100. 相同的树

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

"""

"""
方法一：递归
时间复杂度 : O(N)O(N)，其中 N 是树的结点数，因为每个结点都访问一次。

空间复杂度 : 最优情况（完全平衡二叉树）时为 O(\log(N))O(log(N))，
最坏情况下（完全不平衡二叉树）时为 {O}(N)O(N)，用于维护递归栈。

"""

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        # if not q or not p:
        #     return False

        if type(p) != type(q):
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)


"""
方法二：迭代
"""

from collections import deque

class Solution_2:
    def isSameTree(self, p, q):
        def check(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return True

        deq = deque([(p,q), ])

        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True