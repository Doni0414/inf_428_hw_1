class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        
        res = []

        for x in nums2:
            if x in set1:
                res.append(x)
                set1.remove(x)
        return res