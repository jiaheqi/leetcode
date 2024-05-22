# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 采用二分法找左边界的方法，因为求左边界如果target不存在，返回的是大于target的最小的值的索引，刚好满足题目要求，就是不存在的target需要插入的位置
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 6]
    s = Solution()
    print(s.searchInsert(nums, 3))
# leetcode submit region end(Prohibit modification and deletion)
