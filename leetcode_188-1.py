class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for i in range(1,n+1):
            if i in target:
                lst.append("Push")
            elif i <= max(target):
                lst.append("Push")
                lst.append("Pop")
            else :
                break
        return lst
            
