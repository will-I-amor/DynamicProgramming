#subsequence不是substring，subsequence是[1,2,3,4,5],那么[1,4,5]也属于subsequence
#这道题求不相邻的数的最大sum，2数不相邻
def maxSum(myarr):
    incl = 0
    excl = 0
    for i in myarr:
        temp = incl
        incl = max(incl,excl+i)#incl不是包括i，而是最优的i，前面incl(即不包括现在的i)和包括现在的i+前面的excl
        excl = temp
    return max(incl,excl)
arr1 = [4,1,1,4,2,1]
n = maxSum(arr1)
print n
#incl和excl不能共存么，incl现在的i，之前的i-1就不能要
