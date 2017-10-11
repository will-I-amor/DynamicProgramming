class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        nr = 0
        for i in nums:
            temp = r
            r = nr+i
            nr = max(temp,nr)
        return max(r,nr)
