import os
import sys
import importlib
sys.path.append('test')
#get python file and remove .py
test_files = [test_file[:-3] for test_file in os.listdir("./test") if (test_file[0:4] == "Test")]

for test_module in test_files:
    module = None
    try:
        module = importlib.import_module(test_module, package=None)
    except:
        print(f"error while importing {test_module} test module")
    
    #not running any test if there is error
    if module == None:
        continue
    
    #try run test case
    test_cases = module.tests
    print(f"{test_module}\n")
    for test_case in test_cases:
        try:
            print(f"        {test_case.__name__} is {test_case()}\n")
        except:
             print(f"        {test_case.__name__} is Error\n")