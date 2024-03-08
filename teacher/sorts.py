def BubbleSort(arr):
    """
    冒泡排序：比较相邻元素
    """
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - 1):
            # 核心：比较相邻的元素。如果第一个比第二个大，就交换他们两个
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def SelectSort(arr):
    """选择排序：始终从未排序中找最小
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
    """
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


def InsertSort(arr):
    """插入排序：当前元素插入已排序的合适位置
    将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
    """
    for i in range(len(arr)):
        # 当前需要排序的元素索引
        cur = i
        # 如果当前元素小于已排序的序列最后一个则交换
        while arr[cur - 1] > arr[cur] and cur - 1 > 0:
            arr[cur - 1], arr[cur] = arr[cur], arr[cur - 1]
            # 和有序序列最后一个比较完交换之后，还需要和前面的比较
            cur -= 1
    return arr


def QuickSort(arr, start, end):
    """快速排序:把大于基准小于基准的分别放在两变，终止条件为low和high重合
    """
    # 终止条件是low和high重合
    if start >= end:
        return arr
    mid = arr[start]
    low = start
    high = end
    # 从右往左，如果右边大于基准，那么往左移动
    while high > low and arr[high] > mid:
        high -= 1
    # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
    arr[high] = arr[low]
    # 从左往右，如果左边小于基准，那么往右移动
    while high > low and arr[low] < mid:
        low += 1
    # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处
    arr[low] = arr[high]
    # 退出循环后，low和high重合，重合的位置就是基准元素的位置
    arr[low] = mid
    # 递归排序左右两边
    QuickSort(arr, start, low - 1)
    QuickSort(arr, low + 1, end)
