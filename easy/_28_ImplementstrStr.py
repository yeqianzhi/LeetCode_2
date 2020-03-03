# coding:utf-8

"""
28. 实现 strStr()

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


"""

class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        return haystack.find(needle)


s = Solution()
haystack = ''
needle = 'qw'
result = s.strStr(haystack, needle)
print(result)

"""
string.find(str, beg=0, end=len(string))
检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，
则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
"""