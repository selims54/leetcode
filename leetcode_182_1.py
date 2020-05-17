class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky = []
        for val in set(arr):
            if val == arr.count(val):
                lucky.append(val)
        if len(lucky)==0:
            return -1
        else:
            return max(lucky)


                
            
            
