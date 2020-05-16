# -*- coding: utf-8 -*-

class ThreeStacks(object):
    """ 3.1 Three in One: Describe how you could use a
    single array to implement three stacks.
    """
    def __init__(self, size):
        self.arr = [None] * size
        self.stack1_ptr = 0
        self.stack2_ptr = 1
        self.stack3_ptr = 2

    def pop(self, stack_no):
        pass

    def push(self, stack_no, item):
        if stack_no == 1:
            self.stack1_ptr = self.stack1_ptr + 3
            self.arr[self.stack1_ptr] = item
        elif stack_no == 2:
            self.stack2_ptr = self.stack2_ptr + 3
            self.arr[self.stack2_ptr] = item
        elif stack_no == 3:
            self.stack3_ptr = self.stack3_ptr + 3
            self.arr[self.stack3_ptr] = item
        else:
            raise Exception('stack no {} does not exist'.format(stack_no))

    def peek(self, stack_no):
        if stack_no == 1:
            return self.arr[self.stack1_ptr]
        elif stack_no == 2:
            return self.arr[self.stack2_ptr]
        elif stack_no == 3:
            return self.arr[self.stack3_ptr]
        else:
            raise Exception('stack no {} does not exist'.format(stack_no))

    def is_empty(self, stack_no):
        if stack_no == 1:
            return self.stack1_ptr == 0
        elif stack_no == 2:
            return self.stack2_ptr == 1
        elif stack_no == 3:
            return self.stack3_ptr == 2
        else:
            raise Exception('stack no {} does not exist'.format(stack_no))


