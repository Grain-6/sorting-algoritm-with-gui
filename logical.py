import pandas as pd


def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    sub1 = array[:mid]
    sub2 = array[mid:]

    sub1 = merge_sort(sub1)
    sub2 = merge_sort(sub2)

    return merge(sub1, sub2)


def merge(a1, a2):
    n = len(a1) + len(a2)
    result = [None] * n
    index1, index2 = 0, 0

    while (index1 < len(a1)) and (index2 < len(a2)):
        if a1[index1] <= a2[index2]:
            result[index1 + index2] = a1[index1]
            index1 += 1
        else:
            result[index1 + index2] = a2[index2]
            index2 += 1

        if index1 == len(a1):
            result[index1 + index2:] = a2[index2:]
        else:
            result[index1 + index2:] = a1[index1:]

    return result


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr) - 1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)
    return arr


def partition(arr, start, end):
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    # start = end
    arr[start] = pivot
    return start


class Heap():
    def __init__(self, array):
        self.heap = array
        self.length = len(array)
        self.build_max_heap()

    def left(self, idx):
        pos = 2 * idx + 1
        return pos if pos < self.length else None

    def right(self, idx):
        pos = 2 * idx + 2
        return pos if pos < self.length else None

    def parent(self, idx):
        return (idx - 1) // 2 if idx > 0 else None

    def build_max_heap(self):
        last_to_heapify = self.parent(self.length - 1)
        for i in range(last_to_heapify, -1, -1):
            self.max_heapify(i)

    def _greater_child(self, i):
        left, right = self.left(i), self.right(i)
        if left is None and right is None:
            return None
        elif left is None:
            return right
        elif right is None:
            return left
        else:
            return left if self.heap[left] > self.heap[right] else right

    def max_heapify(self, i):
        greater_child = self._greater_child(i)
        if greater_child is not None and self.heap[greater_child] > self.heap[i]:
            self.heap[i], self.heap[greater_child] = self.heap[greater_child], self.heap[i]
            self.max_heapify(greater_child)

    def sort(self):
        while self.length > 1:
            self.heap[0], self.heap[self.length - 1] = self.heap[self.length - 1], self.heap[0]
            self.length -= 1
            self.max_heapify(0)
        return self.heap


def heap(array):
    return Heap(array).sort()


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self.height = 0


class BST:
    def __init__(self, data_array=[]):
        self.root = None
        for data in data_array:
            self.insert(Node(data))

    def insert(self, new_node, node=0):
        if not self.root:
            self.root = new_node
            return new_node
        if node == 0:
            node = self.root
        if new_node.data < node.data:
            if node.left:
                self.insert(new_node, node.left)
            else:
                new_node.parent = node
                node.left = new_node
        else:
            if node.right:
                self.insert(new_node, node.right)
            else:
                new_node.parent = node
                node.right = new_node

    def sort(self, node=0, result=None):
        if result is None:
            result = []
        if node == 0:
            node = self.root
        if node:
            self.sort(node.left, result)
            result.append(node.data)
            self.sort(node.right, result)
        return result


def BST_sort(array):
    return BST(array).sort()


class AVL(BST):
    def __init__(self, data_array=[]):
        self.root = None
        for data in data_array:
            self.insert(Node(data))

    def insert(self, new_node, node=0):
        super().insert(new_node, node)
        self.check_fix_AVL(new_node.parent)
        return new_node

    def update_all_heights_upward(self, node):
        node.update_height()
        if node is not self.root:
            self.update_all_heights_upward(node.parent)

    def _left_rotate(self, x):
        y = x.right
        B = y.left
        y.parent = x.parent
        y.left = x
        if y.parent is None:
            self.root = y
        elif y.parent.left is x:
            y.parent.left = y
        else:
            y.parent.right = y
        x.parent = y
        x.right = B
        if B is not None:
            B.parent = x
        self.update_all_heights_upward(x)

    def _right_rotate(self, x):
        y = x.left
        B = y.right
        y.parent = x.parent
        y.right = x
        if y.parent is None:
            self.root = y
        elif y.parent.right is x:
            y.parent.right = y
        else:
            y.parent.left = y
        x.parent = y
        x.left = B
        if B is not None:
            B.parent = x
        self.update_all_heights_upward(x)

    def check_fix_AVL(self, node):
        if node is None:
            return
        if abs(node.balance()) < 2:
            self.check_fix_AVL(node.parent)
            return
        if node.balance == 2:
            if node.right.balance() >= 0:
                self._left_rotate(node)
            else:
                self._right_rotate(node.right)
                self._left_rotate(node)
        else:
            if node.left.balance() <= 0:
                self._right_rotate(node)
            else:
                self._left_rotate(node.left)
                self._right_rotate(node)
        self.check_fix_AVL(node.parent)


def AVL_sort(array):
    return AVL(array).sort()


def inerstion_sort(array):
    n = len(array)
    for i in range(1, n):
        temp = array[i]
        for j in range(i):
            if array[j] > array[i]:
                array[j + 1:i + 1] = array[j:i]
                array[j] = temp
    return array


def bubble(array):
    n = len(array)
    while True:
        swapped = False
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if swapped == False:
            break
    return array


def sort_result(data, size, func=None, col=None):
    if func == None:
        result = data
        print("Below is the original 10 rows of the Inquiry System for Taiwan Traffic Data")
        print(result.head(10))
    else:
        sort_origin = data[col]
        sample_size = int(len(sort_origin) * size)
        new_sort = sort_origin[:sample_size]
        result = func(new_sort)
        print("Below is the top 10 rows of the Inquiry System for Taiwan Traffic Data after sorting ")
        print(result.head(10))
        return result.head(10)


def search(frame, keyword=None, data=None):
    str_data = data
    str_data = [str(i) for i in str_data]
    if keyword == None:
        new_data = frame
        print("Below is the original 10 rows of the Inquiry System for Taiwan Traffic Data")
        print(new_data.head(10))
    else:
        find = str(keyword)
        index_find = [i for i, v in enumerate(str_data) if v == find]
        new_data = frame.loc[index_find]
        print("Below is the original 10 rows of the Inquiry System for Taiwan Traffic Data after searching")
        print(new_data.head(10))
    return new_data
