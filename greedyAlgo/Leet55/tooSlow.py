#this version can run ,but too slow, didn't pass
#I calculate from the end of the array
#i-j means distance from the beginning element to the end element
def jump(nums):
    n = len(nums)
    i = n-1
    flag = False
    while (i>0):
        for j in range(i-1,-1,-1):
            if nums[j]>=(i-j):
                tmp = j
                flag = True
                i = j
                break
            else:
                flag = False
        if flag==False:
            break
    return flag

nums1 = [4,0,0,3,0,0,1,4]
nums2 = [2,3,1,1,4]
nums3 = [3,2,1,0,4]
nums4 = [0,2,3]
p = jump(nums)
print p
