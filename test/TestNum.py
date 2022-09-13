import sys

sys.path.append('code')
from Num import *


#test column_at and given_name is none
def test_const_with_none():
    num_module = Num(None,None)
    return num_module.col_at == 0 and num_module.name == ''
#test column_at and given_name is not none
def test_const_with_not_none():
    num_module = Num(1,"col1")
    return num_module.col_at == 1 and num_module.name == 'col1'

#test sort
def test_sort():
    num_module = Num(0,"col1")
    num_module.data=[5,4,3,2,1]
    num_module.nums()
    return num_module.is_sorted and num_module.data == [1,2,3,4,5]

#test sort on empty
def test_sort_on_empty():
    num_module = Num(0,"col1")
    num_module.nums()
    return num_module.is_sorted and num_module.data == []


#test reset sort
def test_reset_sort():
    num_module = Num(0,"col1")
    num_module.add(5)
    num_module.add(4)
    num_module.nums()

    if not num_module.is_sorted:
        return False
    num_module.add(3)
    return not num_module.is_sorted

#test add not reaching capacity
def test_add_no_replace():
    num_module = Num(None,None)
    num_module.add(1)
    num_module.add(2)
    num_module.add(3)
    num_module.add(1)
    #check n
    if num_module.n != 4:
        return False
    
    #check length
    if len(num_module.data) != 4:
        return False
    #check low
    if num_module.low != 1:
        return False
    #check high
    if num_module.high != 3:
        return False
    #check data
    if num_module.data != [1,2,3,1]:
        return False
    return True

# #basically use 2 sample t test to determin if both data comming from same population
# def test_add_with_replacement():
#     from scipy import stats
#     import numpy as np
#     num_module = Num(None,None)
#     #create random population
#     random_population = np.random.normal(0, 250, 500)

#    # random_population = stats.norm.rvs(loc=5, scale=10, size=500, random_state='int')
#     #add rvs1 to num_module
#     for random_num in random_population:
#         num_module.add(random_num)
#     #run t test 
#     p_value = stats.ttest_ind(num_module.data, random_population).pvalue
#     #1 means identical
#     return p_value > 0.85

def test_div():
    num_module = Num(None,None)
    datas = [1,2,3,4,5,8,10,99,77,89,90,77.1]
    for data in datas:
        num_module.add(data)
    return num_module.div() - 40.710 < 0.01
#test std on empty data

def test_div_empty():
    num_module = Num(None,None)
    return num_module.div() is None

def test_div_min():
    num_module = Num(None,None)
    num_module.add(1)
    num_module.add(1)
    return num_module.div() == 0

def test_mid_long_odd():
    num_module = Num(None,None)
    datas = [1,2,3,4,5,6,7,8,9]
    for data in datas:
        num_module.add(data)
    return num_module.mid() == 5

def test_mid_long_even():
    num_module = Num(None,None)
    datas = [1,2,3,4,5,6,7,8]
    for data in datas:
        num_module.add(data)
    return num_module.mid() == 4

def test_mid_single():
    num_module = Num(None,None)
    num_module.add(1)
    return num_module.mid() == 1
    
def test_mid_empty():
    num_module = Num(None,None)
    return num_module.mid() == None


    










tests = [test_const_with_none,test_const_with_not_none,test_sort,test_sort_on_empty,test_reset_sort,test_add_no_replace,test_div,test_div_empty,test_div_min,test_mid_long_odd,test_mid_long_even,test_mid_single,test_mid_empty]

#for development testing 
# for test_case in tests:
#     try:
#         print(f"{test_case.__name__} {'pass' if test_case() else 'failed'}")
#     except:
#          print(f"{test_case.__name__} ERROR!")