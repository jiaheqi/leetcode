import random


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 选择排序：核心思想是每次都找当前数组中最小或者的值，存放到另一个数组中
    # def sortArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #
    #     def find_smallest(nums):
    #         smallest = 0
    #         for i in range(len(nums)):
    #             if nums[i] < nums[smallest]:
    #                 smallest = i
    #         return smallest
    #
    #     res = []
    #     for _ in range(len(nums)):
    #         res.append(nums.pop(find_smallest(nums)))
    #     return res

    # 快速排序：核心是递归+分治，选择一个基准值，将原数组分为大于和小于基准值的两部分，然后分别递归排序这两部分，然后和基准值拼接起来
    def sortArray(self, nums):
        # 当数组只有一个元素或者为空的时候不需要排序，直接返回
        if len(nums) < 2:
            return nums
        flag = random.choice(nums)
        left = [i for i in nums[1:] if i < flag]
        left = self.sortArray(left)
        right = [i for i in nums[1:] if i > flag]
        right = self.sortArray(right)
        # 相同值保留 避免因为大量相同元素造成的算法退化
        mid = [x for x in nums if x == flag]
        return left + mid + right

    # 冒泡排序:比较相邻像个元素的大小，然后互换位置
    # def sortArray(self, nums):
    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] >= nums[j]:
    #                 nums[i], nums[j] = nums[j], nums[i]
    #     return nums


if __name__ == '__main__':
    # nums = [5, 1, 1, 2, 0, 0]
    nums = [5, 2, 3, 1]
    s = Solution()
    print(s.sortArray(nums))

# leetcode submit region end(Prohibit modification and deletion)
