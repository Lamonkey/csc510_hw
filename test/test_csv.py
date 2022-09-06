from code.Data import *
from code.arithmetic import *
file_name = "data/auto93.csv"

num_fails = 0
dump = False
tests = {}
eg = "ALL"

def test_engine():
    # cache/store old status values 
    old_dump = False

    #if the test case exists, execute it
    if eg in tests:
        test_passes = tests[eg]()
    else:
        print("Invalid test case")
    #restore old settings
    dump = old_dump
    if test_passes:
        msg = "PASS"
    else:
        msg = "FAIL"
    print("!!!!!", msg, eg)

def test_all():
    global num_fails
    for _,test in tests.items():
        if test == test_all:
            continue
        if test() == False:
            num_fails = num_fails + 1
    return num_fails == 0

tests["ALL"] = test_all

#define and push test functions
def test_data():
    d= Data(file_name)
    print(d)
    return d != None

tests["data"] = test_data

def test_arithmetic():
    if(1 == 1):
        return True
    return False
tests["arithmetic"] = test_arithmetic

test_engine()