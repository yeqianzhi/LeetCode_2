# coding:utf-8

"""
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""


def isValid(s):
    # 判断是否为空字符串
    hashmap = {'(': ')', '{': '}', '[': ']'}

    if not s:
        print("1")
        return True

    if len(s) % 2 != 0:
        print("2")
        return False

    if s[0] == ')' or s[0] == '}' or s[0] == ']':
        print("3")
        return False

    ls = []


    for i in range(len(s)-1):
        if i == 0:
            ls.append(s[i])
            print("4:", ls)


        if s[i+1] == hashmap[ls[-1]]:
            ls.pop()
            print("5:", ls)
        else:
            ls.append(s[i+1])
            print("6:", ls)

        print("xx", ls)

    if ls:
        print("7:", ls)
        return False
    else:
        print("8:", ls)
        return True


str = "{[]}()"
result = isValid(str)
print(result)


# def isValid(self, s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     temp_str = []  # 存放临时开括号
#     openParentheses = ["(", "[", "{"]
#     combineParentheses = ["()", "[]", "{}"]
#     for cha in s:
#         if cha in openParentheses:  # 如果是开括号就放入temp_str中
#             temp_str.append(cha)
#         else:
#             if not temp_str:  # 如果temp_str为空，返回False
#                 return False
#             else:
#                 temp_cha = temp_str.pop() + cha  # 弹出，组合
#                 if temp_cha not in combineParentheses:
#                     return False
#     if not temp_str:  # 判断是否存在多余开括号
#         return True
#     else:
#         return False