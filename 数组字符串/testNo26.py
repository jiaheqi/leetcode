def removeDuplicates(nums):
    # 外层循环是0到倒数第二位
    for i in range(len(nums) - 1):
        # 内层循环从后开始，终止条件为i=j
        j = len(nums) - 1
        while i < j:
            # 满足条件则删除
            if nums[i] == nums[j]:
                nums.pop(j)
                print(nums)
            j -= 1
    print(nums)
    return len(nums)

if __name__ == '__main__':
    nums = [0, 1, 1, 1, 2, 2, 3, 3, 4]
    removeDuplicates(nums)