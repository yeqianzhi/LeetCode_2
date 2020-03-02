# coding:utf-8

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
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
