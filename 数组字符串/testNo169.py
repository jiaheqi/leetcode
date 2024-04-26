from collections import Counter


def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    majorityElement(nums)
