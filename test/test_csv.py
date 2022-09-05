import pytest 
from code.Data import *
file_name = "data\\auto93.csv"
def test_data(): 
    d = Data(file_name)
    print(d)
    assert(d != None)
