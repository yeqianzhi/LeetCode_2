# coding: utf-8

"""
172. 阶乘后的零

给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
"""
解题关键：
不断除以 5, 是因为每间隔 5 个数有一个数可以被 5 整除, 然后在这些可被 5 整除的数中,
每间隔 5 个数又有一个可以被 25 整除, 故要再除一次, ... 直到结果为 0, 
表示没有能继续被 5 整除的数了.
"""
class Solution:
    def trailingZeroes(self, n):
        # mul = 1
        # for i in range(1, n+1):
        #     mul *= i
        # count = 0
        # strs = str(mul)[::-1]
        # for s in strs:
        #     if s != '0':
        #         return count
        #     count += 1
        #
        # return count

        count = 0
        while n:
            count += int(n // 5)
            n /= 5

        return count

s = Solution()
n = 90
result = s.trailingZeroes(n)
print(result)
