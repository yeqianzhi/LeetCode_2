# coding:utf-8

"""
38. 外观数列

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
解释：这是一个基本样例。
示例 2:

输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。

"""


class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        res = [1, 1]
        for i in range(3, n + 1):
            new_res = []
            num = 1
            cur = res[0]
            for s in res[1:]:
                if s == cur:
                    num += 1
                else:
                    new_res.append(num)
                    new_res.append(cur)
                    num = 1
                    cur = s
            new_res.append(num)
            new_res.append(cur)
            res = new_res
        return ''.join(list(map(str, res)))


s = Solution()
n = 4
result = s.countAndSay(n)
print(result)

# l = [1]
#
# if n == 1:
#     return '1'
#
# index = 0
# count = 1
# for i in range(1, n):
#     new_list = []
#     for j in range(index, len(l)):
#         if index + 1 < len(l) and j+1 < len(l):
#             save = l[index]
#             if save == l[j + 1]:
#                 count += 1
#             else:
#                 index = j + 1
#                 count = 1
#         elif index + 1 == len(l):
#             count = 1
#             save = l[index]
#
#
#         if j + 1 < len(l):
#             new_list.append(count)
#             new_list.append(save)
#
#     l = new_list
#
# return l
