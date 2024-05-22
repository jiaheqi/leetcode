
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        # 如果长度为偶数，返回中间两个数的和/2
        if l % 2 ==0:
            res = (nums[l//2-1] + nums[l//2])/2
        # 如果为长度为奇数，返回最中间的数
        else:
            res = nums[(l-1)//2]
        return res
if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4,5]
    s = Solution()
    s.findMedianSortedArrays(nums1,nums2)
# leetcode submit region end(Prohibit modification and deletion)
