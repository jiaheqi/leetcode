
def quickSort(arr):
    """
    快速排序算法。

    参数:
    arr -- 待排序的列表

    返回值:
    排序后的列表
    """
    # 当列表长度小于等于1时，直接返回该列表，这是递归的终止条件
    if len(arr) <= 1:
        return arr
    # 选择列表的第一个元素作为基准值（pivot）
    pivot = arr[0]
    # 分别收集小于等于基准值和大于基准值的元素
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    # 递归地对小于等于基准值的列表和大于基准值的列表进行排序，最后将它们与基准值合并
    return quickSort(less) + [pivot] + quickSort(greater)

import unittest

class TestQuickSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(quickSort([]), [])

    def test_single_element(self):
        self.assertEqual(quickSort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(quickSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(quickSort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_descending_list(self):
        self.assertEqual(quickSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_list_with_negative_numbers(self):
        self.assertEqual(quickSort([0, -1, -2, -3, -4]), [-4, -3, -2, -1, 0])

    # Add more test cases if needed

if __name__ == '__main__':
    unittest.main()
