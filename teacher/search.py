def sort_search(arr, value):
    """
    顺序查找
    :param arr: 待查找的列表
    :param value: 要找的值
    :return:
    """
    for i in range(len(arr)):
        if arr[i] == value:
            return i


def binary_search(arr, value):
    """
    二分查找
    :param arr: 待查找的列表
    :param value: 要找的值
    :return:
    """
    left = 0
    right = len(arr) - 1
    # 终止条件
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == value:
            return mid
        # 如果中间值比要找的值大，那么要找的值在中间值左边，右坐标左移
        elif arr[mid] > value:
            right -= 1
        # 如果中间值比要找的值小，那么要找的值在中间值右边，左坐标右移
        else:
            left += 1
