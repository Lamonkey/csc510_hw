#test case for Sym module
import sys
sys.path.append('code')

from Sym import *

#test if column_at and given_name is None
def test_none():
    sym_module = Sym(None,None)
    return sym_module.col_at == 0 and sym_module.name == ''


#test if column_at and given_name is not None
def test_not_none():
    sym_module = Sym(1,"test_col")
    return sym_module.col_at == 1 and sym_module.name == 'test_col'

tests = [test_none,test_not_none]