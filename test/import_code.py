#help file in test to acess function under code folder
from os.path import dirname
absolute_path = dirname(__file__)
code_path = "/code"
code_full_path = dirname(absolute_path) + "/code"
import sys
sys.path.append(code_full_path)

from code import *