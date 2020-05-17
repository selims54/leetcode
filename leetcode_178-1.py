class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = []
        for num in nums:
            cnt = 0
            for i in range (len(nums)):                
                if num > nums[i]:
                    cnt+=1
            lst.append(cnt) 
        return lst
