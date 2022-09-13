import sys
from code.cli import Config
from test.test_csv import *

# Parse Command Line, Populate "the" Configuration Object
c = Config()
the = c.cli(sys.argv[1:])

if the["eg"] != "nothing":
    #run some test
    run_test(the["eg"], the)
