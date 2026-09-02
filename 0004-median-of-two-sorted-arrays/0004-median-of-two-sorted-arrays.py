class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        i = 0
        j = 0
        prev = 0
        curr = 0

        for _ in range((m + n) // 2 + 1):
            prev = curr

            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if (m + n) % 2 == 1:
            return curr

        return (prev + curr) / 2