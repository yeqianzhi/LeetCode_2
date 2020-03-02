# coding:utf-8

"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""
"""
1、如何解决问题
遍历寻找，先找到第一个值，用目标值减去第一个值得到差，
然后遍历寻找是否有等于这个差的值
"""


class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for x in range(n):
            b = target - nums[x]
            if b in nums:
                y = nums.index(b)
                if y != x:
                    # return x, y
                    print(x, y)


nums = []
for i in range(4):
    nums.append(int(input()))
target = int(input())
s = Solution()
s.twoSum(nums, target)
