# coding:utf-8


class Solution:
    def longestCommonPrefix(self, strs):
        # 判断是否为空
        if not strs:
            return ""

        # 找到最短的字符串
        shorest = min(strs, key=len)
        print("shorest", shorest)

        # 转换为枚举对象
        for i_th, letter in enumerate(shorest):
            for other in strs:
                if other[i_th] != letter:
                    return shorest[:i_th]

        return shorest




s = Solution()
strs = ["flower","flow","flight"]
result = s.longestCommonPrefix(strs)
print(result)


# def longestCommonPrefix(strs):
#     len_strs = len(strs)
#     min_len = len(strs[0])
#     s = set()
#     for i in range(len_strs):
#         if len(strs[i]) < min_len:
#             min_len = len(strs[i])
#
#     for i in range(min_len):
#         for j in range(len_strs):
#             s.add(strs[j][i])
#         if len(s) > i + 1:
#             print("none")
#
#
#
# strs = ["flower","flow","flight"]
# longestCommonPrefix(strs)

