from tabnanny import check
import import_code
from Row import *
#check copy by value
def check_copy_by_value():
    test_list = [1,2,3,4,5]
    row_module = Row(test_list)
    row_module.cooked[0] = 0
    return test_list == [1,2,3,4,5] and row_module.cooked == [0,2,3,4,5]

tests = [check_copy_by_value]
