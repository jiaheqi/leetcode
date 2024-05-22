# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_bound( nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            if low < 0 or low >= len(nums):
                return -1
            return low if nums[low] == target else -1

        def left_bound2(nums, target):
            low, high = 0, len(nums)
            while low < high:  # 因为区间为右开，所以不需要-1
                mid = (low + high) // 2
                if nums[mid] == target:
                    high = mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid  # 因为区间为右开，所以不需要-1
            if low < 0 or low >= len(nums):
                return -1
            return low if nums[low] == target else -1  # while 循环的终止条件是 low == high，所以返回 low 和 high 是一样的

        def right_bound(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            if high < 0 or high >= len(nums):
                return -1
            return high if nums[high] == target else -1

        def right_bound2(nums, target):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            if high-1 < 0 or high-1 >= len(nums):
                return -1
            return high - 1 if nums[high - 1] == target else -1  # while 循环的终止条件是 low == high，所以返回 low 和 high 是一样的
                        # left = left_bound(nums,target)
        # right = right_bound(nums,target)
        left = left_bound2(nums,target)
        right = right_bound2(nums,target)
        return [left,right]


if __name__ == '__main__':
    nums = [1, 2, 2, 2, 3]
    s = Solution()
    # print(s.left_bound(nums, 2))
    # print(s.right_bound(nums, 2))
    # print(s.right_bound2(nums, 2))
    print(s.searchRange(nums,2))

# leetcode submit region end(Prohibit modification and deletion)
