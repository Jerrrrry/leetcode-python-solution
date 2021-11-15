# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res=0
        data=collections.defaultdict(int)

        for i in nums1:
                for j in nums2:
                        data[i+j]=data.get(i+j,0)+1
        for i in nums3:
                for j in nums4:
                        res+=data[-i-j]
        return res

        
