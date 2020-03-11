# coding: utf-8

"""
225. 用队列实现栈

使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-stack-using-queues
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
使用单队列（list）实现
方法一：使用一个队列，队列添加元素后，反转前n-1个元素，栈顶元素始终保留在队首
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        q_length = len(self.q)
        while q_length > 1:
            self.q.append(self.q.pop(0))
            q_length -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q


"""
方法二：
"""
from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.helper = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.data) > 1:
            self.helper.append(self.data.popleft())
        tmp = self.data.popleft()
        self.helper, self.data = self.data, self.helper
        return tmp

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.data) != 1:
            self.helper.append(self.data.popleft())
        tmp = self.data.popleft()
        self.helper.append(tmp)
        self.helper, self.data = self.data, self.helper
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.data


obj = MyStack()
obj.push(1)
param_2 = obj.pop()
print(param_2)

"""
方法三：
"""
from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.q1:
            self.q2.append(x)
        else:
            self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.q1:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()
        else:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.q1):
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            tmp = self.q1.popleft()
            self.q2.append(tmp)
            return tmp
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            tmp = self.q2.popleft()
            self.q1.append(tmp)
            return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0 and len(self.q2) == 0