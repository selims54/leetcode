class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        team = 0
        if len(rating )< 3:
            return 0
        else:
            n = len (rating) 
            for i in range (n):
                j=i+1
                k=j+1
                while(j<n-1):
                    if (rating[i]<rating [j]):
                        while (k<n):
                            if(rating [j]<rating[k]):
                                team+=1
                            k+=1
                    elif (rating[i]>rating[j]):
                        while (k<n):
                            if(rating[j]>rating[k]):
                                team+=1
                            k+=1
                    j+=1
                    k=j+1
        return team
            
            
            
