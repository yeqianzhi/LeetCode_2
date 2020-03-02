# coding:utf-8

"""
Given a 32-bit signed integer, reverse digits of an integer.
"""

"""
解决方法1：
1、将输入的int转换成str；
2、分不同的情况判断
    正整数还是负整数
    if 正整数，直接转为 int
    if 负整数，判断个位，十位，百位等是否连续为0
        if 连续为0，则去除，在最前面加上符号再反转
        else 先加上负号再反转
"""


class Solution:
    def reverse(self, x):
        if x >= 0:  # 如果为正整数
            x = str(x)  # 转换成字符串
            x = x[::-1]  # 将字符串反转
            if int(x) <= (2 ** 31) - 1:
                return int(x)
            else:
                return 0
        else:
            x = -x
            x = str(x)[::-1]
            if -int(x) >= -1 * (2 ** 31):
                return -int(x)
            else:
                return 0




num = Solution()
x = int(input())
result = num.reverse(x)
print(result)
