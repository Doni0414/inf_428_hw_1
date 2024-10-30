class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left = m - 1
        right = n - 1
        idx = n + m - 1

        while left >= 0 and right >= 0:
            if nums1[left] < nums2[right]:
                nums1[idx] = nums2[right]
                right-=1
            else:
                nums1[idx] = nums1[left]
                left-=1
            idx-=1
        
        while left >= 0:
            nums1[idx] = nums1[left]
            idx-=1
            left-=1

        while right >= 0:
            nums1[idx] = nums2[right]
            idx-=1
            right-=1