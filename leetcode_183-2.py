class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        s_rev = s[::-1]
        num = 0
        for j, val in enumerate(s_rev,0):
            num+=2**j*(int(val))
        if num<2:
            return 0
        while(num>1):
            if num%2==0:
                num/=2
                steps+=1
            else:
                num+=1
                steps+=1
                num/=2
                steps+=1                
        return steps
                    
