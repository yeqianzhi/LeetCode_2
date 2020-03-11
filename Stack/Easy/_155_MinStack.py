# coding:utf-8

"""
155. 最小栈

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
方法一：辅助栈和数据栈同步  
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]


"""
复杂度分析：
时间复杂度：O(1)，“出栈”、“入栈”、“查看栈顶元素”的操作不论数据规模多大，
都只是有限个步骤，因此时间复杂度是：O(1)O(1)。
空间复杂度：O(N)，这里 NN 是读出的数据的个数。
"""

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
方法二：辅助栈和数据栈不同步
"""


class MinStack:

    # 辅助栈和数据栈不同步
    # 关键 1：辅助栈的元素空的时候，必须放入新进来的数
    # 关键 2：新来的数小于或者等于辅助栈栈顶元素的时候，才放入（特别注意这里等于要考虑进去）
    # 关键 3：出栈的时候，辅助栈的栈顶元素等于数据栈的栈顶元素，才出栈，即"出栈保持同步"就可以了

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        top = self.data.pop()
        if self.helper and top == self.helper[-1]:
            self.helper.pop()
        return top

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]
