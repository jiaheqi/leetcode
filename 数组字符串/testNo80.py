def removeDuplicates2(nums):
    # 外层循环是0到倒数第二位
    for i in range(len(nums) - 2):
        # 每个元素的次数计量器，如果大于2则删除
        flag = 1
        # 内层循环从后开始，终止条件为i=j
        j = len(nums) - 1
        while i < j:
            # 满足条件则删除
            if nums[i] == nums[j]:
                flag += 1
                if flag > 2:
                    nums.pop(j)
                    print(nums)
            j -= 1
    return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    removeDuplicates2(nums)
