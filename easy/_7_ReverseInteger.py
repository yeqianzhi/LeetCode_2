# coding:utf-8

"""
7. 整数反转

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

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
