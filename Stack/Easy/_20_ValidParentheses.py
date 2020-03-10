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
    # 定义一个空栈
    stack = []

    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        # 如果是右括号
        if char in mapping:
            # 如果栈不为空，将栈顶的元素弹出
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # 如果该右括号在map中对应的左括号是否与栈顶元素不相等
            if mapping[char] != top_element:
                return False

        # 如果是左括号，直接进栈
        else:
            stack.append(char)

        # 如果 stack 为 0，则 not stack 返回 True
        # 如果 stack 不为 0，则 not stack 返回 False
        return not stack


str = "{[]}()"
result = isValid(str)
print(result)
