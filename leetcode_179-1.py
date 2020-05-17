class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        str = ""
        bgn=97
        if n%2 == 0:
            str+=chr(bgn)
            for i in range(1,n):
                str+=chr(bgn+1)
            return str

        elif n%2 ==1 and n>1:
            str+=chr(bgn)
            str+=chr(bgn+1)
            for i in range(2,n):
                str+=chr(bgn+2)
            return str
        elif n==1:
            str+=chr(bgn)
            return str        
