class area():
    
    def __init__(self,len_1,len_2,len_3):
        self.len_1 = len_1
        self.len_2 = len_2
        self.len_3 = len_3
        
        self.find_area()
        
    def find_area(self):
        
        self.s = (self.len_1+self.len_2+self.len_3)/2
        
        area = (self.s*(self.s-self.len_1)*(self.s-self.len_2)*(self.s-self.len_3))**0.5
        
        return area
        
a=area(6,8,10)
areafound = a.find_area()
print(areafound)
