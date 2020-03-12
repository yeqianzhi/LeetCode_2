# coding: utf-8

"""
496. 下一个更大元素 I

给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
示例 2:

输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
注意:

nums1和nums2中所有元素是唯一的。
nums1和nums2 的数组大小都不超过1000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        执行用时 :
        72 ms, 在所有 Python3 提交中击败了
        53.63%的用户
        内存消耗 :
        13.6 MB, 在所有 Python3 提交中击败了
        5.26%的用户
        :param nums1:
        :param nums2:
        :return:
        """
        """
        解题思路:
        先处理nums2，将nums2中每个元素对应的下一个最大值存入字典中
        利用栈，
        """
        # 存储nums2每个元素对应的下一个最大值的字典
        dict = {}
        # 栈
        stack = []
        # 最后返回的列表
        res = []

        for i in range(len(nums2)):
            # 如果栈不为空，nums2[i]大于栈顶
            while stack and nums2[i] > stack[-1]:
                # 将栈顶弹出,nums[i]存储到dict中
                dict[stack.pop()] = nums2[i]
            # 将nums[i]入栈
            stack.append(nums2[i])

        # 剩下的都是没有下一个最大值
        while stack:
            dict[stack.pop()] = -1

        # 字典一一对应
        for i in range(len(nums1)):
            res.append(dict[nums1[i]])

        return res

        # res = []
        #
        # for i in range(len(nums1)):
        #     index = nums2.index(nums1[i])  # 返回nums1列表某元素在nums2的索引
        #     if index == len(nums2) - 1:
        #         res.append(-1)
        #         continue
        #     for j in range(index+1, len(nums2)):
        #         if nums2[j] > nums1[i]:
        #             res.append(nums2[j])
        #             break
        #     if len(res) == i:
        #         res.append(-1)
        #
        #
        #
        # return res




obj = Solution()
nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]
res = obj.nextGreaterElement(nums1, nums2)
print(res)

