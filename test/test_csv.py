#add code to search 
from os.path import dirname
absolute_path = dirname(__file__)
code_path = "/code"
test_path = "/test"
code_full_path = dirname(absolute_path) + code_path
test_full_path = dirname(absolute_path) + test_path
import sys
sys.path.append(code_full_path)
sys.path.append(test_full_path)

import importlib
from Data import *
from arithmetic import *
from cli import *
from Utility import oo
import sys

def run_test(name, given_the):
    num_fails = 0
    the = given_the.copy()
    tests = {}
    test_cli = "ALL"
    file_name = the["file"]
        
    def test_engine(test):
        nonlocal the
        # cache/store old status values 
        old_the = the.copy()
        crash = False
        status = True
        #if the test case exists, execute it
        if test in tests:
            #https://wiki.python.org/moin/HandlingExceptions
            if the["dump"] == True:
                test_passes = tests[test]()
            else:
                try:
                    test_passes = tests[test]()
                except:
                    crash = True
                    test_passes = False
        else:
            print("Invalid test case")
            return
            
        #restore old settings
        the = old_the.copy()

        #print output
        if test_passes:
            msg = "PASS"
            crash = "false"
        elif crash:
            msg = "CRASH"
            crash = "true"
        else:
            msg = "FAIL"
            crash = "false"
        print("!!!!!!", msg, test, crash)
        return test_passes

    def test_all():
        nonlocal num_fails
        for test_name,test_function in tests.items():
            if test_function == test_all:
                continue
            print("\n-----------------------------------")
            if test_engine(test_name) == False:
                num_fails = num_fails + 1
        print("\n-----------------------------------")
        return True
    tests["ALL"] = test_all

    #define and add test functions to dictionary

    def test_list():
        print("\nExamples py -m test_csv -e ...")
        for name, function in tests.items():
            print("\t", name)
        return True
    tests["LIST"] = test_list

    def test_bad():
        try:
            d=Data()
            #Should crash
            return False
        except:
            return True
    tests["bad"] = test_bad

    def test_arithmetic():
        if(1 == 1):
            return True
        return False
    tests["arithmetic"] = test_arithmetic

    def test_data():
        d = Data(file_name)
        return d.error == False
    tests["data"] = test_data

    #auto adding all test cases 
    test_files = [test_file[:-3] for test_file in os.listdir(test_full_path) if (test_file[0:4] == "Test" and '.py' in test_file)]
    for test_module in test_files:
        module = None
        try:
            module = importlib.import_module(test_module, package=None)
        except:
            print(f"error while importing {test_module} test module")
        
        #not running any test if there is error
        if module == None:
            continue
        
        #adding test cases to dict
        test_cases = module.tests
        print(f"{test_module}\n")
        for test_case in test_cases:
            tests[f"{test_module} {test_case.__name__}"] = test_case
    test_engine(name)
    #https://docs.python.org/2/library/sys.html
    sys.exit(num_fails)

