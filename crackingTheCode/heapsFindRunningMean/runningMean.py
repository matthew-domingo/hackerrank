#!/bin/python3

import sys

class Heap:
    """provides basics for heaps"""
    def __init__(self):
        self.arr = []
    def left_child(self, pos):
        return pos*2 + 1
    def right_child(self, pos):
        return pos*2 + 2
    def parent(self, pos):
        return (pos - 1) // 2
    def has_left_child(self, pos):
        return(len(self.arr) > self.left_child(pos))
    def has_right_child(self, pos):
        return(len(self.arr) > self.right_child(pos))
    def has_parent(self, pos):
        return pos > 0
    def peak(self):
        if len(self.arr) > 0:
            return self.arr[0]
        return 0
    def pop(self):
        if len(self.arr) > 0:
            val = self.arr[0]
            self.arr[0] = self.arr[-1]
            self.arr.pop()
            self.downHeap()
            return val
        return 0
    def downHeap(self):
        pass
    def upHeap(self):
        pass
    def add(self, val):
        self.arr.append(val)
        self.upHeap()
    def size(self):
        return len(self.arr)

class MaxHeap(Heap):

    def __init__(self):
        Heap.__init__(self)

    def downHeap(self):
        pos = 0
        while(self.has_left_child(pos) or self.has_right_child(pos)):
            child = 0
            if self.has_right_child(pos):
                if self.arr[self.left_child(pos)] > self.arr[self.right_child(pos)]:
                    child = self.left_child(pos)
                else:
                    child = self.right_child(pos)
            else:
                child = self.left_child(pos)
            if self.arr[child] > self.arr[pos]:
                self.arr[child], self.arr[pos] = self.arr[pos], self.arr[child]
                pos = child
            else:
                break

    def upHeap(self):
        pos = len(self.arr) - 1
        while(self.has_parent(pos)):
            par = self.parent(pos)
            if self.arr[pos] > self.arr[par]:
                self.arr[pos], self.arr[par] = self.arr[par], self.arr[pos]
                pos = par
            else:
                break

class MinHeap(Heap):

    def __init__(self):
        Heap.__init__(self)

    def downHeap(self):
        pos = 0
        while(self.has_left_child(pos) or self.has_right_child(pos)):
            child = 0
            if self.has_right_child(pos):
                if self.arr[self.left_child(pos)] < self.arr[self.right_child(pos)]:
                    child = self.left_child(pos)
                else:
                    child = self.right_child(pos)
            else:
                child = self.left_child(pos)
            if self.arr[child] < self.arr[pos]:
                self.arr[child], self.arr[pos] = self.arr[pos], self.arr[child]
                pos = child
            else:
                break

    def upHeap(self):
        pos = len(self.arr) - 1
        while(self.has_parent(pos)):
            par = self.parent(pos)
            if self.arr[pos] < self.arr[par]:
                self.arr[pos], self.arr[par] = self.arr[par], self.arr[pos]
                pos = par
            else:
                break

def balanceHeaps(bigHeap, smallHeap):
    while smallHeap.size() > bigHeap.size():
        bigHeap.add(smallHeap.pop())
    while smallHeap.size() < bigHeap.size() - 1:
        smallHeap.add(bigHeap.pop())

n = int(input().strip())
bigHeap = MinHeap()
smallHeap = MaxHeap()
median = 0
is_even = True
for _ in range(n):
    val = int(input().strip())
    if median < val:
        bigHeap.add(val)
    else:
        smallHeap.add(val)
    balanceHeaps(bigHeap, smallHeap)
    is_even = not is_even
    if is_even:
        median = (bigHeap.peak() + smallHeap.peak()) / 2
    else:
        median = bigHeap.peak()
    print("%.1f" % (median))