class Solution:
    def nextpermutation(self,nums:list[int])->None:
        i=len(nums)-2
        while i >=0 and nums[i]>=nums[i+1]:
            i-=1
        
        if i <0:
            nums.reverse()
            return 
        j=i
        while j<len(nums)-1 and nums[j+1]>nums[i]:
            j+=1
        
        nums[i],nums[j]=nums[j],nums[i]

        i,k=i+1,len(nums)-1

        while i<k:
            nums[i],nums[k]=nums[k],nums[i]
            i+=1
            k-=1
