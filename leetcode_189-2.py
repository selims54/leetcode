class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        lst = text.lower().split()
        lst.sort(key=len)
        lst[0]= lst[0].title()
        txt = ''
        for i in lst:
            txt = txt+ i+" "
        return txt.strip()
        
        
