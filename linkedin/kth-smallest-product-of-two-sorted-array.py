#https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

class Solution:
        def kthproduct(self,nums1:list[int],nums2:list[int],k:int)->int:
                a1,a2=[-a for a in nums1 if a<0],[a for a in nums1 if a>=0]
                b1,b2=[-a for a in nums2 if a<0 ],[a for a in nums2 if a>=0]

                neg=len(a1)*len(b2)+len(b1)*len(a2)

                if k>neg:
                        k-=neg
                        s=1
                else:
                        b1,b2=b2,b1
                        s=-1
                        k=neg-k+1

                def count(a,b,m):
                        res=0
                        l=len(b)-1
                        for i in range(len(a)):
                                while l>=0 and a[i]*b[l]>m:
                                        l-=1
                                res+=l+1
                        return res
                l=0
                r=10**10

                while l<r:
                        m=(l+r)//2
                        if count(a1,b1,m)+count(a2,b2,m)>=k:
                                r=m
                        else:
                                l=m+1
                return l*s
