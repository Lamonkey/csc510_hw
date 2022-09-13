import math

class Utility:
    
    def per(t, p):
        '''return p-th thing from sorted list t'''
        p = math.floor(((p if p else 0.5) * len(t)) + 0.5)
        return t[max(1, min(len(t), p))]