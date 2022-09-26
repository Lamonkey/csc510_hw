import math
import re

# class Utility:
    
def per(t, p=0.5):
    '''return p-th thing from sorted list t'''
    p = math.floor((p * len(t)) + 0.5)
    return t[max(1, min(len(t), p)) - 1]

#TODO o and oo may not be properly implemented. Not sure how to address sorting with lua tables vs python dicts
def o(t):
    if type(t) is not dict: #TODO is dict the table equivalent?    
        vars_t = vars(t)
        vars_t['data'] = "Hidden..."    
        return vars_t
    def show(k,v):
        if not re.find("^_", str(k)):
            v = o(v)
            return len(t) == 0 and ":{} {}".format(k,v) or str(v)
    u = {}
    for k,v in t.items():
        u[1+len(u)] = show(k, v)
    output = ""
    for k,v in u.items():
        output += "{}{}".format(k,v)
    return "{" + output + "}"

def oo(t):
    print( o(t) )
    return t