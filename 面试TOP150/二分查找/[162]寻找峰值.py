# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # def findPeakElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     left, right = 0, len(nums) - 1
    #     # 处理特殊情况，数组只有一个元素
    #     if right == 0:
    #         return 0
    #     while left <= right:
    #         # 处理边界情况
    #         if left == right == 0 and nums[left] > nums[left + 1] or left == right == len(nums) - 1 and nums[left] > \
    #                 nums[left - 1]:
    #             return left
    #
    #         mid = (left + right) // 2
    #         if nums[mid - 1] < nums[mid] > nums[mid + 1]:
    #             return mid
    #         elif nums[mid] > nums[mid + 1]:
    #             right = mid - 1
    #         elif nums[mid] <= nums[mid + 1]:
    #             left = mid + 1
    #
    #     return left

    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 2
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:  # 说明mid+1在峰顶右侧
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    # nums = [1, 2, 1, 3, 5, 6, 4]
    # nums = [1, 2, 3, 1]
    # nums = [1, 2, 3]
    # nums = [4, 3, 2, 1, 4]
    nums = [4, 5, 6, 7, 0, 1, 2]
    s = Solution()
    print(s.findPeakElement(nums))

# leetcode submit region end(Prohibit modification and deletion)
