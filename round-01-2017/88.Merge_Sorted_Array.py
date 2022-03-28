# -*- coding: utf-8 -*-


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        if not m:
            nums1[:] = nums2[:n]
            return

        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]

        p = 0
        q = 0

        while p < len(nums1) and q < len(nums2):
            # print nums1[p], nums2[q]
            if nums1[p] >= nums2[q]:
                nums1.insert(p, nums2[q])
                nums2.pop(q)
                p += 1
                n -= 1
            else:
                p += 1
        if nums2:
            nums1 += nums2[:n]

        print nums1

s = Solution()
s.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5)
s.merge([1,0],1,[2],1)
s.merge([0],0,[1],1)
