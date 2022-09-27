#add code to search 
import sys
from os.path import dirname
absolute_path = dirname(__file__)
code_path = "/code"
test_path = "/test"
code_full_path = dirname(absolute_path) + code_path
test_full_path = dirname(absolute_path) + test_path
sys.path.append(code_full_path)
sys.path.append(test_full_path)
from cli import Config
from test_engine import *

# Parse Command Line, Populate "the" Configuration Object
c = Config()
the = globals()['the'] = c.cli(sys.argv[1:])

if the["eg"] != "nothing":
    #run some test
    run_test(the["eg"], the)
