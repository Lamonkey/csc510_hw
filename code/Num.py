import random as rn
from Utility import *

class Num:
    def __init__(self, column_at, given_name):
        self.n = 0
        self.low = max
        self.high = min
        self.col_at = column_at if column_at != None else 0
        self.name = given_name if given_name != None else ''
        self.is_sorted = False
        self.data = []
        self.w = -1 if given_name != None and given_name[-1] == '-' else 1
        
    def nums(self):
        if not self.is_sorted:
            self.data.sort()
            self.is_sorted = True
        return self.data
    
    def add(self, v, the): #TODO should 'the' be a parameter? or a global var somewhere?
        if v != '?':
            self.n += 1
            self.low = min(v, self.low)
            self.high = max(v, self.high)
        if len(self.data) < the.nums:
            pos = 1 + len(self.data)
        elif rn.random() < the.nums/self.n:
            pos = rn.randint(0, len(self.data) - 1)
        if pos:
            self.is_sorted = False
            self.data[pos] = float(v) # TODO float or int?
    
    def div(self):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1))/2.58
    
    def mid(self):
        return per(self.nums(), 0.5)
            
