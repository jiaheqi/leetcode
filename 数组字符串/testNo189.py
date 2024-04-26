def rotate(nums, k):
    for _ in range(k):
        nums.insert(0, nums.pop())
    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    # nums = [1]
    # k = 0
    print(rotate(nums, k))
