# coding:utf-8

"""
67. 二进制求和

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

"""

class Solution1:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


"""
int(x, base = 10)
x -- 字符串或数字。
base -- 进制数，默认十进制。

bin(x)
x -- int 或者 long int 数字
>>>bin(10)
'0b1010'
>>> bin(20)
'0b10100'
"""
