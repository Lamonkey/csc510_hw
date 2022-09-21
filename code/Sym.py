import math

class Sym:
    """Representation of a Symbol column. Contains a column_at column, a counter (n), and a given name.
    Defines interface for adding symbols, and mid and div functions for summaries of the data."""
    def __init__(self, column_at, given_name):
        self.n = 0
        self.col_at = column_at if column_at != None else 0
        self.name = given_name if given_name != None else ''
        self.data = {} # note: lua code appears to be list but should be dict (probably)
    
    def add(self, v):
        '''add one thing to col'''
        if v != '?':
            self.n += 1
            self.data[v] = self.data.setdefault(v, 0) + 1 #https://docs.python.org/3/library/stdtypes.html#dict.setdefault
    #return None if data is empty
    def mid(self): #TODO does col, most, or mode need to be a parameter?
        most = -1
        mode = None
        for k,v in self.data.items():
            if v > most:
                mode, most = k, v
        return mode
    
    def div(self): #TODO does e or fun need to be a parameter?
        e = 0
        def fun(p):
            return p*math.log(p,2)
        for _,n in self.data.items():
            e = e - fun(n/self.n)
        return e