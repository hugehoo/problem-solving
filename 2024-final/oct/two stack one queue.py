class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def push(self, x: int) -> None:
        self.stack_in.append(x)
    
    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
    
    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
    
    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


#
# q = MyQueue()
# q.push(1)
# q.push(2)
# q.push(3)
# print(q.stack_in, q.stack_out)
# print(q.peek())
# print(q.pop())
# print(q.stack_in, q.stack_out)
# print(q.pop())
# print(q.stack_in, q.stack_out)
# print(q.empty())
# print(q.pop())
# print(q.empty())

class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def push(self, x: int) -> None:
        self.stack_in.append(x)
    
    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
    
    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
    
    def empty(self) -> bool:
        return len(self.stack_out) == 0 and len(self.stack_in) == 0


class Queue3(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, x: int) -> None:
        self.in_stack.append(x)
    
    def is_empty(self):
        return not self.in_stack and not self.out_stack
    
    def dequeue(self) -> int:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.out_stack.pop()
    
    def __repr__(self):
        temp = []
        temp += self.out_stack[::-1]
        temp += self.in_stack
        if temp:
            return repr(temp)
        else:
            return "Queue is empty"


class Queue2:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, value):
        self.in_stack.append(value)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        # out_stack 이 비어있는지 확인해야함 -> 그렇지 않으면 무조건 in_stack 의 요소를 out_stack 에 넣게 되는데,
        # 이러면 아직 출력되지 않은 out_stack 의 요소가 출력되지 않은채 남아있는 상황이 발생하기 때문이다.
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
    
    def is_empty(self):
        return not self.out_stack and not self.in_stack


# class Queue2(object):
#     def __init__(self):
#         self.in_stack = []
#         self.out_stack = []
#
#     def isEmpty(self):
#         return not (bool(self.in_stack) or bool(self.out_stack))
#
#     def enqueue(self, item):
#         return self.in_stack.append(item)
#
#     def dequeue(self):
#         if not self.out_stack:
#             while self.in_stack:
#                 self.out_stack.append(self.in_stack.pop())
#         if self.isEmpty():
#             print("Queue is empty!")
#         else:
#             return self.out_stack.pop()
#
#     def __repr__(self):
#         tmp = []
#         tmp += self.out_stack[::-1]
#         tmp += self.in_stack
#         if tmp:
#             return repr(tmp)
#         else:
#             return "Queue is empty!"


q = Queue2()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
# print(q.in_stack, q.out_stack)
print(q.dequeue())
# print(q.in_stack, q.out_stack)
print(q.dequeue())
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
# print(q.in_stack, q.out_stack)
print(q.is_empty())
print(q.dequeue())
print(q.is_empty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())

# q = Queue()
# q.push(1)
# q.push(2)
# q.push(3)
# print(q.stack_in, q.stack_out)
# print(q.peek())
# print(q.pop())
# print(q.stack_in, q.stack_out)
# print(q.pop())
# q.push(4)
# q.push(5)
# q.push(6)
# print(q.stack_in, q.stack_out)
# print(q.empty())
# print(q.pop())
# print(q.empty())
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())
