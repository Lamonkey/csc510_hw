import sys
sys.path.append('code')
from Num import *

#test Num.low 
def test_low():
    return False
#test Num.high
def test_high():
    return False
#test column_at and given_name is none
def test_none():
    num_module = Num(None,None)
    return num_module.col_at == 0 and num_module.given_name == ''
#test column_at and given_name is not none
def test_not_none():
    num_module = Num(1,"col1")
    return num_module.col_at == 1 and num_module.given_name == 'col1'
#test sort
def test_sort():
    return False
#test w
def test_w():
    return False

tests = [test_low,test_high,test_none,test_not_none,test_sort,test_w]