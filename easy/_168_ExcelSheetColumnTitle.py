# coding:utf-8

"""
168. Excel表列名称

给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
对于题目的疑惑？？？
是要从Excel中读取吗？不是
这些序号对应的列名称有一定规律
"""

class Solution:
    def convertToTitle(self, n):

        hashmap = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F',
                   7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
                   13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R',
                   19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
                   25: 'Y', 26: 'Z', 0: 'Z'}

        if 1 <= n <= 26:
            return hashmap[n]

        result = ''

        while 1:
            shang = n // 26
            print("shang", shang)
            remain = n % 26
            print("remain", remain)
            n = shang
            print("n", n)
            if remain == 0:
                n -= 1
            result += hashmap[remain]
            print("result", result)
            if n == 0:
                return result[::-1]

        # res = ''
        # while n > 0:
        #     mod = int((n-1) % 26)
        #     num = int(65 + mod)
        #     res += chr(num)
        #     n = (n - 1) / 26
        #
        # return res[::-1]






s = Solution()
n = 2
result = s.convertToTitle(n)
print(result)