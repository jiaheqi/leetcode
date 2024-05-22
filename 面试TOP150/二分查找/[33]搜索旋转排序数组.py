# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 找旋转点
        def find_min(nums):
            left = 0
            right = len(nums) - 2
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[-1]:  # mid是在旋转点右侧的区间，mid右侧一定是有序的，染色蓝色，right左移
                    right = mid - 1
                else:  # 否则，mid是在旋转点左侧的区间，mid左侧一定是有序的，染色蓝色，left右移
                    left = mid + 1
            return left  # 最终left和right重合的位置其实就是最小值的位置，因为还满足while，此时nums[mid] < nums[-1]，right = mid - 1 ，所以最终最小值的位置是left或者right +1

        # 在有序数组查找
        def left_bound(nums, target):

            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:  # target一定在mid右侧，left右移
                    left = mid + 1
                else:
                    right = mid - 1
            return -1


        k = find_min(nums)
        print(k)
        left_search = nums[:k]
        right_search = nums[k:]
        ans = left_bound(left_search, target)
        print(f'left ans:{ans}')
        if ans == -1:
            ans = left_bound(right_search, target)
            print(f'right ans:{ans}')
            if ans == -1:
                return ans
            else:
                return ans + k  # 因为如果是右区间求出的索引，换算到原来的整个数组，那么需要加上k
        else:
            return ans


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [3,1]
    # print(nums[4:])
    s = Solution()
    print(s.search(nums, 3))

# leetcode submit region end(Prohibit modification and deletion)
