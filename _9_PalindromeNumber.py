# coding:utf-8

# 回文数


class Solution:
    def isPalindrome(self, x):
        str_1 = str(x)
        str_2 = str_1[::-1]
        if str_1 == str_2:
            return True
        else:
            return False

s = Solution()
x = int(input())
result = s.isPalindrome(x)
print(result)