# coding: utf-8

"""
面试题 03.04. 化栈为队

实现一个MyQueue类，该类用两个栈来实现一个队列。


示例：

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

说明：

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        tmp = self.stack_2.pop()
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return tmp

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        tmp = self.stack_2[-1]
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_1


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_3, param_2, param_4)