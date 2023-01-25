
def findMedianSortedArrays(nums1, nums2):
    
    joinedList = nums1 + nums2
    joinedList.sort()
    
    if len(joinedList)%2 == 0:
        index = len(joinedList)//2
        val1 = joinedList[index]
        val2 = joinedList[(index) - 1]
        
        return (val1+val2)/2
    else:
        index = len(joinedList)//2
        val1 = joinedList[index]
        return val1
    
    
    
    
nums1 = [1,3]
nums2 = [2]

out = findMedianSortedArrays(nums1, nums2)
print(out)