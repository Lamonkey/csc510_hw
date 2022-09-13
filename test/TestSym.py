
import import_code
from Sym import *
#test constructor
def test_const_with_none():
    sym_module = Sym(None,None)
    return sym_module.col_at == 0 and sym_module.name == ''

def test_const_with_not_none():
    sym_module = Sym(1,"test_col")
    return sym_module.col_at == 1 and sym_module.name == 'test_col'

#test on different input
def test_div_1():
    sym_module = Sym(None,None)
    sym_module.add("test_sym_1")
    sym_module.add("test_sym_1")
    sym_module.add("test_sym_1")
    sym_module.add("test_sym_2")
    sym_module.add("test_sym_2")
    sym_module.add("test_sym_3")
    return sym_module.div() - 1.4591479 < 0.001

#test empty case
def test_div_2():
    sym_module = Sym(None,None)
    return sym_module.div() == 0
    
def test_succes_add():
    sym_module = Sym(None,None)
    sym_module.add("test_sym_1")
    sym_module.add("test_sym_2")
    sym_module.add("test_sym_1")
    sym_module.add("test_sym_3")
    #there should be 2 sym_1, 1 sym_2, 1 sym_3 and 0 sym_4
    if sym_module.data['test_sym_1'] != 2:
        return False
    if sym_module.data['test_sym_2'] != 1:
        return False
    if sym_module.data['test_sym_3'] != 1:
        return False
    if "test_sym_4" in sym_module.data:
        return False
    #total 4
    if sym_module.n != 4:
        return False
    return True

#data size should be zero
def test_fail_add():
    sym_module = Sym(None,None)
    sym_module.add("?")
    return len(sym_module.data.keys()) == 0 and sym_module.n ==0
    
def test_mid_non_empty():
    sym_module = Sym(None,None)
    sym_module.add("test_sym_1")
    sym_module.add("test_sym_2")
    sym_module.add("test_sym_1")
    sym_module.add("test_sym_3")
    #there should be 2 sym_1, 1 sym_2, 1 sym_3 and 0 sym_4
    return sym_module.mid() == "test_sym_1"

def test_mid_empty():
    sym_module = Sym(None,None)
    #there should be 2 sym_1, 1 sym_2, 1 sym_3 and 0 sym_4
    return sym_module.mid() is None
tests = [test_div_2,test_mid_empty,test_const_with_none,test_const_with_not_none,test_div_1,test_succes_add,test_mid_non_empty,test_fail_add]

# for development testing  
# for test_case in tests:
#     print(f"{test_case.__name__} {'pass' if test_case() else 'failed'}")