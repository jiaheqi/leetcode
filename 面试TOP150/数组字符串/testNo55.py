def canJump(nums):
    rightmost = 0
    for i in range(len(nums)):
        # 如果当前位置大于上一个位置能到达的最远位置，说明当前位置是上一个位置无法道德的位置，那么直接return false
        if i <= rightmost:
            if rightmost >= len(nums) - 1:
                return True
            else:
                rightmost = max(rightmost, nums[i] + i)
    return False


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    # nums = [1, 1, 1, 0]
    nums = [0, 2, 3]
    print(canJump(nums))
