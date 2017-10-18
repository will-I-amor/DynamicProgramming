    Find the contiguous subarray within an array (containing at least one number) which has the largest product.

    For example, given the array [2,3,-2,4],
    the contiguous subarray [2,3] has the largest product = 6.
    这道题是用DP来求最大subArray的乘积。subArray是必须要连续的，不能隔开。subsequence可以隔开
    
    乘积需要注意的地方就是 负负为正。  这次最min的数，乘以一个负数，有可能就变成最大的数了。因此需要3个数来记录
    #建3个数，maxCur, minCur和product
    #maxCur = max(maxCur*nums[i],minCur*nums[i],nums[i])
    #minCur = min(maxCur*nums[i],minCur*nums[i],nums[i])
    #product = max(maxCur,product)
