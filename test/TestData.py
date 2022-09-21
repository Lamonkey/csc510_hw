import sys

sys.path.append('code')

from Data import *
from Utility import oo

#load csv file into data
def test_load_data():
    file_name = "data/auto93.csv"
    d = Data(file_name)
    for n in range(0,10):
        oo(d.rows[n].cells)
        #test a couple values
    return True

tests = [test_load_data]