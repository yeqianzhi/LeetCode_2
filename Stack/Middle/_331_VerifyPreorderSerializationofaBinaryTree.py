# coding:utf-8

"""
331. 验证二叉树的前序序列化

序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1:

输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true
示例 2:

输入: "1,#"
输出: false
示例 3:

输入: "9,#,#,1"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
初始化可用槽位为 1：slots = 1。

遍历前序序列化字符串，每遍历到逗号字符：

空节点和非空节点都消耗一个槽位：slots = slot - 1。

如果当前可用槽位是负数，那么这个先序序列就是非法的，返回 False。

非空节点（即逗号字符前不是 #），新增两个可用槽位：slots = slots + 2`。

最后一个节点需要单独处理，因为最后一个节点后面是没有逗号的。

如果可用槽位全部被消耗完，那么该前序序列化就是合法的：返回 slots == 0。

作者：LeetCode
链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/solution/yan-zheng-er-cha-shu-de-qian-xu-xu-lie-hua-by-leet/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 槽位
        slots = 1

        prev = None # 当前的字符
        for ch in preorder:
            if ch == ',':
                # 遇到一个‘,’就消耗一个槽位
                slots -= 1

                # 如果槽位为负数
                if slots < 0:
                    return False

                # 如果当前不为‘#’
                if prev != '#':
                    slots += 2
            prev = ch

        # 特殊的最后一个字符
        slots = slots + 1 if ch != '#' else slots - 1
        # 所有的槽位都要用掉
        return slots == 0





