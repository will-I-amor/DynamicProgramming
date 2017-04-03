#subsequence不是substring，subsequence是[1,2,3,4,5],那么[1,4,5]也属于subsequence
#这道题求不相邻的数的最大sum，2数不相邻
def maxSum(myarr):
    incl = 0
    excl = 0
    for i in myarr:
        temp = incl
        incl = max(incl,excl+i)
        excl = temp
    return max(incl,excl)
arr1 = [4,1,1,4,2,1]
n = maxSum(arr1)
print n
