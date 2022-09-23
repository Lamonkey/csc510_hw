import sys

sys.path.append('code')

from Data import *
from Utility import oo

#load csv file into data
def test_load_file():
    file_name = "data/auto93.csv"
    d = Data(file_name)
    for n in range(0,10):
        oo(d.rows[n].cells)
        #test a couple values
    return True

#print some stats on columns
def test_stats():
    file_name = "data/auto93.csv"
    #load in data from a file
    d = Data(file_name)

    #calculate mid for x columns and y columns
    x_cols = d.cols.x_columns
    y_cols = d.cols.y_columns

    print("xmid", d.stats(3, x_cols, "mid"))
    print("xdiv", d.stats(3, x_cols, "div"))
    print("ymid", d.stats(3, y_cols, "mid"))
    print("ydiv", d.stats(3, y_cols, "div"))

    return True
tests = [test_load_file, test_stats]