class Solution(object):
    def findLengthOfLCIS(self, nums):
        maxLength = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
            else:
                count = 1
            maxLength = max(maxLength, count)
        return maxLength