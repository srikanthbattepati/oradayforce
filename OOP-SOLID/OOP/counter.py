class Counter:
    def __init__(self): 
        self.value = 0
        
    def incr(self):
        self.value =  self.value + 1
        return self.value
    
    def decr(self):
        self.value =  self.value - 1
        return self.value
    
    def incrby(self,n):
        self.value =  self.value + n
        return self.value
    
    def decrby(self,n):
        self.value =  self.value - n
        return self.value

