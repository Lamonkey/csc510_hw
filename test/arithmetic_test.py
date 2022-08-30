import pytest 
from code.arithmetic import *

def test_add():
    assert add_numbers(1,2) == 3

def test_subtract():
    assert subtract_numbers(2,1) == 1