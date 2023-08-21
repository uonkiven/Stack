'''
视频来源：https://www.bilibili.com/video/BV1VC4y1x7uv?p=15&vd_source=85c07e7dc542842b10c667ea5480ec64

栈：是一种有次序的数据项集合，在栈中，数据项的加入和移除都仅发生在同一端。这一端叫栈顶top，另一端叫栈底base。

距离栈底越近的数据项留在栈中的时间就越长，而最新加入栈的数据项会被最先移除
这种次序通常被称为“后进先出LIFO”：Last in First out

栈的特性：反转次序

抽象数据类型Stack
抽象数据类型”栈“的定义如下操作：
Stack():创建一个空栈，不包含任何数据项。
push(item):将item加入栈项，无返回值。
pop():将栈顶数据移除，并返回，栈被修改。
peek():”窥视“栈顶数据项，返回栈顶的数据项但不移除，栈不会被修改。
isEmpty():返回栈是否为空栈。
size():返回栈中有多少个数据项。
'''

# 用Python实现 ADT Stack
#Python的面向对象机制，可以用来实现用户自定义类型
#将ADT Stack实现为Python的一个Class

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
