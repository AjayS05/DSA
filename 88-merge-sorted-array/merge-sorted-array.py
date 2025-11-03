class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        
        while i < m+n and j < n:
            if nums2[j] < nums1[i]:
                nums1.insert(i,nums2[j])
                i+=1
                j+=1
                nums1.pop(-1)
            elif i>=m+j and nums1[i]==0:
                nums1[i]=nums2[j]
                i+=1
                j+=1             
            else:
                i+=1
            