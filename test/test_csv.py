from code.Data import *
from code.arithmetic import *
import sys
file_name = "../data/auto93.csv"

num_fails = 0
dump = False
tests = {}
test_cli = "ALL"

def test_engine(test):
    # cache/store old status values 
    old_dump = False

    crash = False
    status = True
    #if the test case exists, execute it
    if test in tests:
        #https://wiki.python.org/moin/HandlingExceptions
        try:
            test_passes = tests[test]()
        except:
            crash = True
            test_passes = False
    else:
        print("Invalid test case")
        return
    #restore old settings
    dump = old_dump

    #print output
    if test_passes:
        msg = "PASS"
    elif crash:
        msg = "CRASH"
    else:
        msg = "FAIL"
    print("!!!!!!", msg, test)
    return test_passes

def test_all():
    global num_fails
    for test_name,test_function in tests.items():
        if test_function == test_all:
            continue
        print("\n-----------------------------------")
        if test_engine(test_name) == False:
            num_fails = num_fails + 1
    return True
tests["ALL"] = test_all

#define and add test functions to dictionary

def test_bad():
    d=Data()
    return d != None
tests["bad"] = test_bad

def test_list():
    print("\nExamples py -m test_csv -e ...")
    for name, function in tests.items():
        print("\t", name)
    return True
tests["LIST"] = test_list

def test_arithmetic():
    if(1 == 1):
        return True
    return False
tests["arithmetic"] = test_arithmetic

def test_data():
    d= Data(file_name)
    return d != None
tests["data"] = test_data

test_engine(test_cli)
#https://docs.python.org/2/library/sys.html
sys.exit(num_fails)