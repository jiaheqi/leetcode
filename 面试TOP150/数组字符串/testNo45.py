def Jump(nums):
    max_pos = 0
    step = 0
    end = 0
    for i in range(len(nums) - 1):
        max_pos = max(max_pos, nums[i] + i)
        if i == end:
            end = max_pos
            step += 1
    return step


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    # nums = [1, 1, 1, 0]
    # nums = [0, 2, 3]
    print(Jump(nums))
