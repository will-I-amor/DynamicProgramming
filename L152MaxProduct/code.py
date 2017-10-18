def getMax(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
def getMin(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c
def maxProduct(nums):
    if(len(nums)==0): return 0
    curMax = nums[0]
    curMin = nums[0]
    product = nums[0]
    for i in range(1,len(nums)):
        tempMax = curMax
        curMax = getMax(curMax*nums[i],curMin*nums[i],nums[i])
        curMin = getMin(tempMax*nums[i],curMin*nums[i],nums[i])
        product = max(curMax,product)
    print("max product is:", product)
nums = [-1,2,-3,2,1]
maxProduct(nums)
