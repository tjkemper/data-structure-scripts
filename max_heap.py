from math import log, ceil, floor
from pretty_print_util import get_spaces_array, print_slashes


class MaxHeap:
    """A max heap with all the fixings.

    Attributes:
        _heap   The max heap.
    """

    def __init__(self, array):
        """Initialize max heap.

        :param array: an array (of non-negative numbers) to make a max heap.
        """
        self._heap = array
        self.build_max_heap()

    def build_max_heap(self):
        """Build max heap."""
        for index in range(int(self.size() / 2), -1, -1):
            self.max_heapify(index)

    def max_heapify(self, index):
        """Makes subtree (rooted at index) a max heap.

        ASSERT: left and right subtrees (of index) are max heaps.

        :param index: The index to make a max heap.
        """
        violation = self.violation(index)
        if violation == 1:
            self.swap(index, self.left(index))
            self.max_heapify(self.left(index))
        elif violation == 2:
            self.swap(index, self.right(index))
            self.max_heapify(self.right(index))

    def swap(self, i1, i2):
        """Swap keys at index i1 and i2"""
        temp = self._heap[i1]
        self._heap[i1] = self._heap[i2]
        self._heap[i2] = temp

    def violation(self, index):
        """Determines if key at index violates max heap invariant.

        :param index: index of heap to check for violation.
        :return: 0 if no violation.
                 1 if violation and left  child is the max.
                 2 if violation and right child is the max.
        """
        left = self.left(index)
        right = self.right(index)
        left_vio = left < self.size() and self._heap[index] < self._heap[left]
        right_vio = right < self.size() and self._heap[index] < self._heap[right]

        if left_vio != right_vio:  # xor
            if left_vio:
                return 1
            else:
                return 2
        elif left_vio and right_vio:
            if self._heap[self.left(index)] > self._heap[self.right(index)]:
                return 1  # left child is max
            else:
                return 2  # right child is max
        else:
            return 0  # no violation

    def max(self):
        """Return max key.

         If size of heap is 0, then return -1.
         """
        return self._heap[0] if self.size() > 0 else -1

    def extract_max(self):
        """Remove and return max key.

        If size of heap is 0, then returns -1.
        """
        max_key = self.max()
        if max_key != -1:
            self.swap(0, self.size() - 1)
            self._heap = self._heap[:-1]
            self.max_heapify(0)
        return max_key

    def size(self):
        """Return size of max heap."""
        return len(self._heap)

    def height(self):
        """Return height of max heap."""
        return ceil(log(self.size() + 1, 2))

    def increase_key(self, index, new_key):
        """Increase the key at index to new_key.

        :param index: The key to increase.
        :param new_key:  The new value.
        """
        if self._heap[index] < new_key:  # check if we're increasing the key at index.
            self._heap[index] = new_key
            while index > 0 and self._heap[MaxHeap.parent(index)] < self._heap[index]:
                self.swap(index, MaxHeap.parent(index))
                index = MaxHeap.parent(index)

    def insert(self, key):
        """Insert value into max heap."""
        self._heap.append(-1)
        self.increase_key(self.size() - 1, key)

    def sorted_array(self):
        """Return sorted array. Empties heap."""
        sorted_array = []
        for i in range(self.size()):
            sorted_array.append(self.extract_max())
        return sorted_array

    @staticmethod
    def left(index):
        """Return index of left child."""
        return 2 * index + 1

    @staticmethod
    def right(index):
        """Return index of right child."""
        return 2 * index + 2

    @staticmethod
    def parent(index):
        """Return index of parent."""
        return floor((index - 1) / 2)

    def pretty_print(self):
        """Pretty print max heap."""
        if self.size() == 0:
            print("Max heap is empty.")
            return

        height = self.height()
        spaces = get_spaces_array(height)
        num_keys = 1
        index = 0

        for h in range(height, 0, -1):
            print(" " * spaces[h - 1], end="")
            for i in range(num_keys):
                if index >= self.size():
                    break  # Break if we've printed all keys.
                num_spaces = " " * spaces[h]
                print(str(self._heap[index]) + num_spaces, end="")
                index += 1

            print()
            print_slashes(h, spaces, num_keys)
            num_keys *= 2  # The number of keys doubles each level.
