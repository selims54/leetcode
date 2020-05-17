class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.items = []
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.items)<self.maxSize:
            self.items.append(x)
        return self.items

    def pop(self):
        """
        :rtype: int
        """
        if len(self.items) != 0:
            self.items.pop()
            if len(self.items)==0
                return self.items
            else:
                return self.items[-1]
        else:
            return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """

        if len (self.items)>= k:
            for i in range(k):
                self.items[i] += val
            return self.items
        else:
            for i in range (len(self.items)):
                self.items[i] += val
            return self.items
            
        
        
