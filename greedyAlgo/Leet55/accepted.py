def jump(nums):
    if len(nums)==1:
        return True
    else:
        n = len(nums)
        last = n-1
        for i in range(n-2,-1,-1):
            if i+nums[i]>=last:
                last = i
        if last==0:
            return True
        else:
            return False
        
nums1 = [4,0,0,3,0,0,1,4]
p = jump(nums1)
print p
