
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-2
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < nums[-1]:
                right = mid -1
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    nums = [3,4,5,1,2]
    s = Solution()
    print(s.findMin(nums))
